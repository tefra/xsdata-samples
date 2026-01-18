from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass(kw_only=True)
class RailBookingInfo:
    """
    Links journeys and fares together.

    Parameters
    ----------
    rail_fare_ref
        Reference to a fare that applies to the journey below.
    rail_journey_ref
        Reference to a journeys on which the above fare applies.
    optional_service
        Indicate the OfferFareItem elements  will be Optional or not.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_fare_ref: str = field(
        metadata={
            "name": "RailFareRef",
            "type": "Attribute",
            "required": True,
        }
    )
    rail_journey_ref: str = field(
        metadata={
            "name": "RailJourneyRef",
            "type": "Attribute",
            "required": True,
        }
    )
    optional_service: bool = field(
        default=False,
        metadata={
            "name": "OptionalService",
            "type": "Attribute",
        },
    )
