from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class AgencySellInfo5:
    """
    Information about the agency selling the reservation.

    Parameters
    ----------
    iata_code
        The IATA code that pertains to this Agency and Branch.
    country
        The country code of the requesting agency.
    currency_code
        The currency code in which the reservation will be ticketed.
    provider_code
        The IATA assigned airline/GDS code.
    pseudo_city_code
        The PCC in the host system.
    city_code
        IATA code of "home" city or airport.
    """

    class Meta:
        name = "AgencySellInfo"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    iata_code: None | str = field(
        default=None,
        metadata={
            "name": "IataCode",
            "type": "Attribute",
            "max_length": 8,
        },
    )
    country: None | str = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Attribute",
            "length": 2,
        },
    )
    currency_code: None | str = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Attribute",
            "length": 3,
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
    pseudo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        },
    )
    city_code: None | str = field(
        default=None,
        metadata={
            "name": "CityCode",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
