from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.option import Option

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FlightOption:
    """
    List of Options available for any search air leg.

    Parameters
    ----------
    option
        List of BookingInfo available for the search air leg.
    leg_ref
        Identifies the Leg Reference for this Flight Option.
    origin
        The IATA location code for this origination of this entity.
    destination
        The IATA location code for this destination of this entity.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    option: list[Option] = field(
        default_factory=list,
        metadata={
            "name": "Option",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    leg_ref: None | str = field(
        default=None,
        metadata={
            "name": "LegRef",
            "type": "Attribute",
        },
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        },
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        },
    )
