from dataclasses import dataclass, field
from typing import Optional

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
    order_detail: Optional[OrderDetail] = field(
        default=None,
        metadata={
            "name": "OrderDetail",
            "type": "Element",
        },
    )
    order_summary: Optional[OrderSummary] = field(
        default=None,
        metadata={
            "name": "OrderSummary",
            "type": "Element",
        },
    )
