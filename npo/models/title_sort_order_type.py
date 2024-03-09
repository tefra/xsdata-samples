from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.media_sort_type import MediaSortType
from npo.models.owner_type_enum import OwnerTypeEnum
from npo.models.textual_type_enum import TextualTypeEnum

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class TitleSortOrderType(MediaSortType):
    class Meta:
        name = "titleSortOrderType"

    type_value: None | TextualTypeEnum = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    owner: None | OwnerTypeEnum = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
