from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.base_media_type import BaseMediaType
from npo.models.group_type_enum import GroupTypeEnum

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass(kw_only=True)
class GroupType(BaseMediaType):
    class Meta:
        name = "groupType"

    po_series_id: None | str = field(
        default=None,
        metadata={
            "name": "poSeriesID",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    is_ordered: bool = field(
        metadata={
            "name": "isOrdered",
            "type": "Attribute",
            "required": True,
        }
    )
    type_value: GroupTypeEnum = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
    default_element: None | int = field(
        default=None,
        metadata={
            "name": "defaultElement",
            "type": "Attribute",
        },
    )
