from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.media_sort_type_enum import MediaSortTypeEnum
from npo.models.order_type_enum import OrderTypeEnum

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class MediaSortType:
    class Meta:
        name = "mediaSortType"

    value: MediaSortTypeEnum = field(
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
