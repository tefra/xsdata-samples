from __future__ import annotations

from dataclasses import dataclass, field

from xcbl.models.order_request import OrderDetail
from xcbl.models.order_response import (
    OrderHeader,
    OrderSummary,
)


@dataclass(kw_only=True)
class Order:
    order_header: OrderHeader = field(
        metadata={
            "name": "OrderHeader",
            "type": "Element",
            "required": True,
        }
    )
    order_detail: OrderDetail | None = field(
        default=None,
        metadata={
            "name": "OrderDetail",
            "type": "Element",
        },
    )
    order_summary: OrderSummary | None = field(
        default=None,
        metadata={
            "name": "OrderSummary",
            "type": "Element",
        },
    )
