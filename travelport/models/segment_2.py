from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.segment_remark_2 import SegmentRemark2
from travelport.models.type_element_status_3 import TypeElementStatus3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class Segment2:
    """
    The base segment type.

    Parameters
    ----------
    segment_remark
    key
    status
        Status of this segment.
    passive
    travel_order
        To identify the appropriate travel sequence for Air/Car/Hotel
        segments/reservations based on travel dates. This ordering is
        applicable across the UR not provider or traveler specific
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    """

    class Meta:
        name = "Segment"

    segment_remark: list[SegmentRemark2] = field(
        default_factory=list,
        metadata={
            "name": "SegmentRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
            "max_occurs": 999,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        },
    )
    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        },
    )
    passive: None | bool = field(
        default=None,
        metadata={
            "name": "Passive",
            "type": "Attribute",
        },
    )
    travel_order: None | int = field(
        default=None,
        metadata={
            "name": "TravelOrder",
            "type": "Attribute",
        },
    )
    el_stat: None | TypeElementStatus3 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        },
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        },
    )
