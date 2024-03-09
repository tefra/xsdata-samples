from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class PointOfCommencement1:
    """Point of Commencement is optional.

    CityOrAirportCode and date portion of the Time attribute is
    mandatory.

    Parameters
    ----------
    city_or_airport_code
        Three digit Airport or City code that would be the Point of
        Commencement location for the trips/legs mentioned.
    time
        Specify a date or date and time
    """

    class Meta:
        name = "PointOfCommencement"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    city_or_airport_code: None | str = field(
        default=None,
        metadata={
            "name": "CityOrAirportCode",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        },
    )
    time: None | str = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Attribute",
            "required": True,
        },
    )
