from datetime import date
from flask import Flask, request

from allocation.adapters import orm
from allocation.domain import events
from allocation.service_layer import handlers, messagebus, unit_of_work


orm.start_mappers()
app = Flask(__name__)


@app.route("/allocate", methods=["POST"])
def allocate_endpoint():
    try:
        event = events.AllocationRequired(
            request.json["orderid"], request.json["sku"], request.json["qty"])
        results = messagebus.handle(event, unit_of_work.SqlAlchemyUnitOfWork())
        batchref = results.pop(0)
    except handlers.InvalidSku as e:
        return {"message": str(e)}, 400

    return {"batchref": batchref}, 201


@app.route("/batch", methods=["POST"])
def add_batch_endpoint():
    eta = request.json["eta"]
    if eta is not None:
        eta = date.fromisoformat(eta)

    event = events.BatchCreated(request.json["ref"], request.json["sku"], request.json["qty"], eta)
    messagebus.handle(event, unit_of_work.SqlAlchemyUnitOfWork())
    return "OK", 201
