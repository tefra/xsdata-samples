from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_element_status_3 import TypeElementStatus3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class SeatAssignment2:
    """
    Parameters
    ----------
    key
    status
    seat
    seat_type_code
        The 4 letter SSR code like SMSW,NSSW,SMST etc.
    segment_ref
    flight_details_ref
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    rail_coach_number
        Coach number for which rail seatmap/coachmap is returned.
    """

    class Meta:
        name = "SeatAssignment"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    status: str = field(
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
            "length": 2,
            "white_space": "collapse",
        }
    )
    seat: str = field(
        metadata={
            "name": "Seat",
            "type": "Attribute",
            "required": True,
        }
    )
    seat_type_code: None | str = field(
        default=None,
        metadata={
            "name": "SeatTypeCode",
            "type": "Attribute",
            "length": 4,
            "white_space": "collapse",
        },
    )
    segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
        },
    )
    flight_details_ref: None | str = field(
        default=None,
        metadata={
            "name": "FlightDetailsRef",
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
    rail_coach_number: None | str = field(
        default=None,
        metadata={
            "name": "RailCoachNumber",
            "type": "Attribute",
        },
    )
