from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_segment_sell_failure_info import (
    AirSegmentSellFailureInfo,
)
from travelport.models.booking_base_rsp import BookingBaseRsp

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingAirSegmentRsp(BookingBaseRsp):
    """
    Returns sold segments and sell messages.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    air_segment_sell_failure_info: None | AirSegmentSellFailureInfo = field(
        default=None,
        metadata={
            "name": "AirSegmentSellFailureInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
