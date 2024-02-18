from collections.abc import Callable, Mapping
from typing import Any

from allocation.domain import events
from allocation.service_layer import unit_of_work

from . import handlers


def handle(event: events.Event, uow: unit_of_work.AbstractUnitOfWork) -> list[Any]:
    # HACK: Temporary return
    results = []
    queue = [event]
    while queue:
        event = queue.pop(0)
        for handler in HANDLERS[type(event)]:
            results.append(handler(event, uow=uow))
            queue.extend(uow.collect_new_events())
    return results


HANDLERS: Mapping[type[events.Event], list[Callable]] = {
    events.AllocationRequired: [handlers.allocate],
    events.BatchCreated: [handlers.add_batch],
    events.BatchQuantityChanged: [handlers.change_batch_quantity],
    events.OutOfStock: [handlers.send_out_of_stock_notification],
}
