from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_exchange_bundle_list import AirExchangeBundleList
from travelport.models.air_exchange_bundle_total import AirExchangeBundleTotal
from travelport.models.air_segment_data import AirSegmentData

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirExchangeMultiQuoteOption:
    """
    The shared object list of AirExchangeMultiQuoteOptions.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment_data: list[AirSegmentData] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentData",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    air_exchange_bundle_total: None | AirExchangeBundleTotal = field(
        default=None,
        metadata={
            "name": "AirExchangeBundleTotal",
            "type": "Element",
        },
    )
    air_exchange_bundle_list: list[AirExchangeBundleList] = field(
        default_factory=list,
        metadata={
            "name": "AirExchangeBundleList",
            "type": "Element",
            "max_occurs": 999,
        },
    )
