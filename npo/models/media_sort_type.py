from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.media_sort_type_enum import MediaSortTypeEnum
from npo.models.order_type_enum import OrderTypeEnum

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaSortType:
    class Meta:
        name = "mediaSortType"

    value: None | MediaSortTypeEnum = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    order: None | OrderTypeEnum = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
