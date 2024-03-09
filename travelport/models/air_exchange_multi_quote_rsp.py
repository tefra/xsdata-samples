from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_exchange_mulit_quote_list import (
    AirExchangeMulitQuoteList,
)
from travelport.models.air_segment_list import AirSegmentList
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.brand_list import BrandList

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirExchangeMultiQuoteRsp(BaseRsp1):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment_list: list[AirSegmentList] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentList",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    brand_list: list[BrandList] = field(
        default_factory=list,
        metadata={
            "name": "BrandList",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    air_exchange_mulit_quote_list: list[AirExchangeMulitQuoteList] = field(
        default_factory=list,
        metadata={
            "name": "AirExchangeMulitQuoteList",
            "type": "Element",
            "max_occurs": 999,
        },
    )
