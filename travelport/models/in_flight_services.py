from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class InFlightServices:
    """Available InFlight Services.

    They are: 'Movie', 'Telephone', 'Telex', 'AudioProgramming', 'Television' ,'ResvBookingService' ,'DutyFreeSales' ,'Smoking' ,'NonSmoking' ,'ShortFeatureVideo' ,'NoDutyFree' ,'InSeatPowerSource' ,'InternetAccess' ,'Email' ,'Library' ,'LieFlatSeat' ,'Additional service(s) exists' ,'WiFi' ,'Lie-Flat seat first' ,'Lie-Flat seat business' ,'Lie-Flat seat premium economy' ,'Amenities subject to change' etc.. These follow the IATA standard. Please see the IATA standards for a more complete list.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
