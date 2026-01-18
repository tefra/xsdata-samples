from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class PlusUpType:
    """
    Attributes:
        amount: Amount
        origin_city: Origin City
        destination_city: Destination City
        fare_origin_city: Fare Origin City
        fare_destination_city: Fare Destination City
        via_city: Via City
        message: Message
        country_of_payment: Country of payment
    """

    amount: Decimal = field(
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
            "fraction_digits": 3,
        }
    )
    origin_city: str = field(
        metadata={
            "name": "OriginCity",
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    destination_city: str = field(
        metadata={
            "name": "DestinationCity",
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    fare_origin_city: None | str = field(
        default=None,
        metadata={
            "name": "FareOriginCity",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        },
    )
    fare_destination_city: None | str = field(
        default=None,
        metadata={
            "name": "FareDestinationCity",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        },
    )
    via_city: None | str = field(
        default=None,
        metadata={
            "name": "ViaCity",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        },
    )
    message: None | str = field(
        default=None,
        metadata={
            "name": "Message",
            "type": "Attribute",
        },
    )
    country_of_payment: None | str = field(
        default=None,
        metadata={
            "name": "CountryOfPayment",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{2}",
        },
    )
