from collections.abc import Callable, Mapping
from allocation.adapters import email
from allocation.domain import events


def handle(event: events.Event) -> None:
    for h in HANDLERS[type(event)]:
        h(event)


def send_out_of_stock_notification(event: events.OutOfStock):
    email.send_mail("stock@made.com", f"Out of stock for {event.sku}")


HANDLERS: Mapping[type[events.Event], list[Callable]] = {
    events.OutOfStock: [send_out_of_stock_notification]
}
