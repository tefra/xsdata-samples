from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.order_type_enum import OrderTypeEnum
from npo.models.page_sort_type_enum import PageSortTypeEnum

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class PageSortType:
    class Meta:
        name = "pageSortType"

    value: PageSortTypeEnum = field(
        metadata={
            "required": True,
        }
    )
    order: None | OrderTypeEnum = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
