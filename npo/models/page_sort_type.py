from dataclasses import dataclass, field
from typing import Optional
from npo.models.order_type_enum import OrderTypeEnum
from npo.models.page_sort_type_enum import PageSortTypeEnum

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class PageSortType:
    class Meta:
        name = "pageSortType"

    value: Optional[PageSortTypeEnum] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    order: Optional[OrderTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
