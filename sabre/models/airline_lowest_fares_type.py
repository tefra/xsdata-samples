from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.company_name_type import CompanyNameType
from sabre.models.currency_amount_type import CurrencyAmountType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class AirlineLowestFaresType:
    """
    IntelliSell Type . lowest fare for airline.

    Currently not used.
    """

    airline: CompanyNameType = field(
        metadata={
            "name": "Airline",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    no_stops: int = field(
        metadata={
            "name": "NoStops",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    lowest_fare: CurrencyAmountType = field(
        metadata={
            "name": "LowestFare",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    itinerary_count: None | object = field(
        default=None,
        metadata={
            "name": "ItineraryCount",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
