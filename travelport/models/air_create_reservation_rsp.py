from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_segment_sell_failure_info import (
    AirSegmentSellFailureInfo,
)
from travelport.models.air_solution_changed_info import AirSolutionChangedInfo
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.universal_record import UniversalRecord

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class AirCreateReservationRsp(BaseRsp1):
    """
    Parameters
    ----------
    universal_record
    air_solution_changed_info
        Provider: 1G,1V,1P,ACH.
    air_segment_sell_failure_info
        Provider: 1G,1V,1P,ACH.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record: None | UniversalRecord = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
        },
    )
    air_solution_changed_info: list[AirSolutionChangedInfo] = field(
        default_factory=list,
        metadata={
            "name": "AirSolutionChangedInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    air_segment_sell_failure_info: None | AirSegmentSellFailureInfo = field(
        default=None,
        metadata={
            "name": "AirSegmentSellFailureInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
