from dataclasses import dataclass, field
from typing import Optional
from npo.models.media_sort_type import MediaSortType
from npo.models.owner_type_enum import OwnerTypeEnum
from npo.models.textual_type_enum import TextualTypeEnum

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class TitleSortOrderType(MediaSortType):
    class Meta:
        name = "titleSortOrderType"

    type: Optional[TextualTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
