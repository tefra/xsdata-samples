from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_segment_details import AirSegmentDetails
from travelport.models.passenger_details import PassengerDetails

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirItineraryDetails:
    """
    Itinerary details containing brand details.

    Parameters
    ----------
    air_segment_details
    passenger_details
    key
        Air itinerary details key
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment_details: list[AirSegmentDetails] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentDetails",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 16,
        }
    )
    passenger_details: list[PassengerDetails] = field(
        default_factory=list,
        metadata={
            "name": "PassengerDetails",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 15,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
