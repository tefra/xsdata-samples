from __future__ import annotations

from dataclasses import dataclass

from travelport.models.booking_base_rsp import BookingBaseRsp

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass(kw_only=True)
class BookingDisplayRsp(BookingBaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"
