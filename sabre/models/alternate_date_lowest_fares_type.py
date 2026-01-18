from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.currency_amount_type import CurrencyAmountType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class AlternateDateLowestFaresType:
    """
    IntelliSell Type . lowest fare for alternate departure / return date
    times.
    """

    departure_date_time: str = field(
        metadata={
            "name": "DepartureDateTime",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    returnl_date_time: str = field(
        metadata={
            "name": "ReturnlDateTime",
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
