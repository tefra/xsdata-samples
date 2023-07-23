from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_itinerary import TypeItinerary
from travelport.models.type_itinerary_option import TypeItineraryOption

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Itinerary:
    """
    Allows an agency to select the itinenary option for ticket.

    Parameters
    ----------
    type_value
        Specifies the type of itinenary option for ticket like Invoice type
        or Pocket itinenary.
    option
        Specifies the itinerary option like NoFare,NoAmount.
    separate_indicator
        Set to true if one itinerary to be printed per passenger.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    type_value: None | TypeItinerary = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    option: None | TypeItineraryOption = field(
        default=None,
        metadata={
            "name": "Option",
            "type": "Attribute",
        }
    )
    separate_indicator: None | bool = field(
        default=None,
        metadata={
            "name": "SeparateIndicator",
            "type": "Attribute",
        }
    )
