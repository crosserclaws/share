from typing import Any
import uuid


def random_suffix():
    return uuid.uuid4().hex[:6]


def random_sku(name: Any = ""):
    return f"sku-{name}-{random_suffix()}"


def random_batchref(name: Any = ""):
    return f"batch-{name}-{random_suffix()}"


def random_orderid(name: Any = ""):
    return f"order-{name}-{random_suffix()}"
