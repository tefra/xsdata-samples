from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.provider_reservation_status import ProviderReservationStatus

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class UniversalRecordCancelRsp(BaseRsp1):
    """
    Return status for each provider reservation.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    provider_reservation_status: list[ProviderReservationStatus] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationStatus",
            "type": "Element",
            "max_occurs": 999,
        }
    )
