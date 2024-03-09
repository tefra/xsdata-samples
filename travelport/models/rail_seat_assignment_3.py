from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.characteristic_5 import Characteristic5
from travelport.models.type_element_status_4 import TypeElementStatus4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class RailSeatAssignment3:
    """
    Identifies the seat assignment for a passenger on RailSegment.

    Parameters
    ----------
    characteristic
    key
    status
    seat
    rail_segment_ref
    coach_number
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
        name = "RailSeatAssignment"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    characteristic: list[Characteristic5] = field(
        default_factory=list,
        metadata={
            "name": "Characteristic",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
            "length": 2,
            "white_space": "collapse",
        },
    )
    seat: None | str = field(
        default=None,
        metadata={
            "name": "Seat",
            "type": "Attribute",
            "required": True,
        },
    )
    rail_segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "RailSegmentRef",
            "type": "Attribute",
        },
    )
    coach_number: None | str = field(
        default=None,
        metadata={
            "name": "CoachNumber",
            "type": "Attribute",
        },
    )
    el_stat: None | TypeElementStatus4 = field(
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
