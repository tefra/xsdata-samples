from dataclasses import dataclass, field
from typing import Optional
from npo.models.media_sort_type_enum import MediaSortTypeEnum
from npo.models.order_type_enum import OrderTypeEnum

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaSortType:
    class Meta:
        name = "mediaSortType"

    value: Optional[MediaSortTypeEnum] = field(
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
