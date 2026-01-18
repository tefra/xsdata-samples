from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass(kw_only=True)
class TypeStartEndTime:
    """
    Used to specify earliest and latest pickup/dropoff times for a vehicle.

    Parameters
    ----------
    time
        The time in 24 hour clock format.
    requirement_passed
        When true, the time requirement has been met.
    mon
    tue
    wed
    thu
    fri
    sat
    sun
    """

    class Meta:
        name = "typeStartEndTime"

    time: str = field(
        metadata={
            "name": "Time",
            "type": "Attribute",
            "required": True,
        }
    )
    requirement_passed: None | bool = field(
        default=None,
        metadata={
            "name": "RequirementPassed",
            "type": "Attribute",
        },
    )
    mon: None | bool = field(
        default=None,
        metadata={
            "name": "Mon",
            "type": "Attribute",
        },
    )
    tue: None | bool = field(
        default=None,
        metadata={
            "name": "Tue",
            "type": "Attribute",
        },
    )
    wed: None | bool = field(
        default=None,
        metadata={
            "name": "Wed",
            "type": "Attribute",
        },
    )
    thu: None | bool = field(
        default=None,
        metadata={
            "name": "Thu",
            "type": "Attribute",
        },
    )
    fri: None | bool = field(
        default=None,
        metadata={
            "name": "Fri",
            "type": "Attribute",
        },
    )
    sat: None | bool = field(
        default=None,
        metadata={
            "name": "Sat",
            "type": "Attribute",
        },
    )
    sun: None | bool = field(
        default=None,
        metadata={
            "name": "Sun",
            "type": "Attribute",
        },
    )
