from dataclasses import dataclass, field
from typing import Optional
from npo.models.base_media_type import BaseMediaType
from npo.models.group_type_enum import GroupTypeEnum

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class GroupType(BaseMediaType):
    class Meta:
        name = "groupType"

    po_series_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "poSeriesID",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    is_ordered: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isOrdered",
            "type": "Attribute",
            "required": True,
        }
    )
    type: Optional[GroupTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    default_element: Optional[int] = field(
        default=None,
        metadata={
            "name": "defaultElement",
            "type": "Attribute",
        }
    )
