from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.location_6 import Location6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass(kw_only=True)
class CityOrAirport6(Location6):
    """
    This element can be used when it is not known whether the value is an
    airport or a city code.

    Parameters
    ----------
    code
        The airport or city IATA code.
    prefer_city
        Indicates that the search should prefer city results over airport
        results.
    """

    class Meta:
        name = "CityOrAirport"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    code: str = field(
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    prefer_city: bool = field(
        default=False,
        metadata={
            "name": "PreferCity",
            "type": "Attribute",
        },
    )
