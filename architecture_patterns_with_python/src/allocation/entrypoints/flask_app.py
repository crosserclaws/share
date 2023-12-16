from datetime import date
from flask import Flask, request

from allocation.adapters import orm
from allocation.domain import model
from allocation.service_layer import services, unit_of_work


orm.start_mappers()
app = Flask(__name__)


@app.route("/allocate", methods=["POST"])
def allocate_endpoint():
    try:
        batchref = services.allocate(
            request.json["orderid"],
            request.json["sku"],
            request.json["qty"],
            unit_of_work.SqlAlchemyUnitOfWork(),
        )
    except (model.OutOfStock, services.InvalidSku) as e:
        return {"message": str(e)}, 400

    return {"batchref": batchref}, 201


@app.route("/batch", methods=["POST"])
def add_batch_endpoint():
    eta = request.json["eta"]
    if eta is not None:
        eta = date.fromisoformat(eta)

    services.add_batch(
        request.json["ref"],
        request.json["sku"],
        request.json["qty"],
        eta,
        unit_of_work.SqlAlchemyUnitOfWork(),
    )
    return "OK", 201
