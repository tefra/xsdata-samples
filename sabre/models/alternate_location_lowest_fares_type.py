from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.currency_amount_type import CurrencyAmountType
from sabre.models.response_location_type import ResponseLocationType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class AlternateLocationLowestFaresType:
    """
    IntelliSell Type . lowest fare for alternate origin / destination pair.
    """

    origin_location: None | ResponseLocationType = field(
        default=None,
        metadata={
            "name": "OriginLocation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        },
    )
    destination_location: None | ResponseLocationType = field(
        default=None,
        metadata={
            "name": "DestinationLocation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        },
    )
    lowest_fare: None | CurrencyAmountType = field(
        default=None,
        metadata={
            "name": "LowestFare",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        },
    )
