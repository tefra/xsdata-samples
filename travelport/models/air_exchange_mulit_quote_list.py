from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_exchange_multi_quote_option import (
    AirExchangeMultiQuoteOption,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirExchangeMulitQuoteList:
    """
    The shared object list of AirExchangeMultiQuotes.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_exchange_multi_quote_option: list[AirExchangeMultiQuoteOption] = field(
        default_factory=list,
        metadata={
            "name": "AirExchangeMultiQuoteOption",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
