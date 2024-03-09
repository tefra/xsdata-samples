from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class TaxDetail1:
    """
    The tax idetail nformation for a fare quote tax.
    """

    class Meta:
        name = "TaxDetail"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        },
    )
    origin_airport: None | str = field(
        default=None,
        metadata={
            "name": "OriginAirport",
            "type": "Attribute",
            "length": 3,
        },
    )
    destination_airport: None | str = field(
        default=None,
        metadata={
            "name": "DestinationAirport",
            "type": "Attribute",
            "length": 3,
        },
    )
    country_code: None | str = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Attribute",
        },
    )
    fare_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "FareInfoRef",
            "type": "Attribute",
        },
    )
