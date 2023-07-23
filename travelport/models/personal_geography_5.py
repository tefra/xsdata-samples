from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class PersonalGeography5:
    """
    Personal geography details of the associated passenger.

    Parameters
    ----------
    country_code
        Passenger country code.
    state_province_code
        Passenger state/province code.
    city_code
        Passenger city code.
    """
    class Meta:
        name = "PersonalGeography"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    country_code: None | str = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Element",
            "length": 2,
        }
    )
    state_province_code: None | str = field(
        default=None,
        metadata={
            "name": "StateProvinceCode",
            "type": "Element",
            "max_length": 6,
        }
    )
    city_code: None | str = field(
        default=None,
        metadata={
            "name": "CityCode",
            "type": "Element",
            "length": 3,
        }
    )
