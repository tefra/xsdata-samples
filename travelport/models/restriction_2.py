from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Restriction2:
    """
    Fare Reference associated with the BookingRules.
    """

    class Meta:
        name = "Restriction"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    days_of_week_restriction: list[Restriction2.DaysOfWeekRestriction] = field(
        default_factory=list,
        metadata={
            "name": "DaysOfWeekRestriction",
            "type": "Element",
            "max_occurs": 3,
        },
    )
    restriction_passenger_types: list[
        Restriction2.RestrictionPassengerTypes
    ] = field(
        default_factory=list,
        metadata={
            "name": "RestrictionPassengerTypes",
            "type": "Element",
            "max_occurs": 999,
        },
    )

    @dataclass
    class DaysOfWeekRestriction:
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
        restriction_exists_ind: None | bool = field(
            default=None,
            metadata={
                "name": "RestrictionExistsInd",
                "type": "Attribute",
            },
        )
        application: None | str = field(
            default=None,
            metadata={
                "name": "Application",
                "type": "Attribute",
            },
        )
        include_exclude_use_ind: None | bool = field(
            default=None,
            metadata={
                "name": "IncludeExcludeUseInd",
                "type": "Attribute",
            },
        )

    @dataclass
    class RestrictionPassengerTypes:
        max_nbr_travelers: None | str = field(
            default=None,
            metadata={
                "name": "MaxNbrTravelers",
                "type": "Attribute",
            },
        )
        total_nbr_ptc: None | str = field(
            default=None,
            metadata={
                "name": "TotalNbrPTC",
                "type": "Attribute",
            },
        )
