from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1
from travelport.models.currency_conversion import CurrencyConversion

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class CurrencyConversionReq(BaseReq1):
    """
    Performs A Currency Conversion between two Currencies.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    currency_conversion: list[CurrencyConversion] = field(
        default_factory=list,
        metadata={
            "name": "CurrencyConversion",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
