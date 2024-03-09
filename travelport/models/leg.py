from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.leg_detail import LegDetail

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Leg:
    """
    Information about the journey Leg.

    Parameters
    ----------
    leg_detail
    key
    group
        Returns the Group Number for the leg.
    origin
        Returns the origin airport or city code for the leg.
    destination
        Returns the destination airport or city code for the leg.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    leg_detail: list[LegDetail] = field(
        default_factory=list,
        metadata={
            "name": "LegDetail",
            "type": "Element",
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
    group: None | int = field(
        default=None,
        metadata={
            "name": "Group",
            "type": "Attribute",
            "required": True,
        },
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        },
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        },
    )
