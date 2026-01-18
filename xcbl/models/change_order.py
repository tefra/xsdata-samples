from dataclasses import dataclass, field
from typing import Optional

from xcbl.models.order_response import (
    ChangeOrderHeader,
    ChangeOrderItemDetail,
    ChangeOrderPackageDetail,
    OriginalOrderSummary,
    RevisedOrderSummary,
)


@dataclass(kw_only=True)
class ChangeOrderSummary:
    original_order_summary: OriginalOrderSummary | None = field(
        default=None,
        metadata={
            "name": "OriginalOrderSummary",
            "type": "Element",
        },
    )
    revised_order_summary: RevisedOrderSummary | None = field(
        default=None,
        metadata={
            "name": "RevisedOrderSummary",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfChangeOrderItemDetail:
    change_order_item_detail: list[ChangeOrderItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "ChangeOrderItemDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfChangeOrderPackageDetail:
    change_order_package_detail: list[ChangeOrderPackageDetail] = field(
        default_factory=list,
        metadata={
            "name": "ChangeOrderPackageDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ChangeOrderDetail:
    list_of_change_order_item_detail: ListOfChangeOrderItemDetail | None = (
        field(
            default=None,
            metadata={
                "name": "ListOfChangeOrderItemDetail",
                "type": "Element",
            },
        )
    )
    list_of_change_order_package_detail: ListOfChangeOrderPackageDetail | None = field(
        default=None,
        metadata={
            "name": "ListOfChangeOrderPackageDetail",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ChangeOrder:
    change_order_header: ChangeOrderHeader = field(
        metadata={
            "name": "ChangeOrderHeader",
            "type": "Element",
            "required": True,
        }
    )
    change_order_detail: ChangeOrderDetail | None = field(
        default=None,
        metadata={
            "name": "ChangeOrderDetail",
            "type": "Element",
        },
    )
    change_order_summary: ChangeOrderSummary | None = field(
        default=None,
        metadata={
            "name": "ChangeOrderSummary",
            "type": "Element",
        },
    )
