from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.currency_conversion import CurrencyConversion

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class CurrencyConversionRsp(BaseRsp1):
    """
    The response to the CurrencyConversionReq.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    currency_conversion: list[CurrencyConversion] = field(
        default_factory=list,
        metadata={
            "name": "CurrencyConversion",
            "type": "Element",
            "max_occurs": 999,
        },
    )
