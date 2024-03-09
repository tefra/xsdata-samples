from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.child_provider_reservation_info import (
    ChildProviderReservationInfo,
)
from travelport.models.parent_provider_reservation_info import (
    ParentProviderReservationInfo,
)

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class ProviderReservationDivideRsp(BaseRsp1):
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    parent_provider_reservation_info: None | ParentProviderReservationInfo = (
        field(
            default=None,
            metadata={
                "name": "ParentProviderReservationInfo",
                "type": "Element",
                "required": True,
            },
        )
    )
    child_provider_reservation_info: None | ChildProviderReservationInfo = (
        field(
            default=None,
            metadata={
                "name": "ChildProviderReservationInfo",
                "type": "Element",
                "required": True,
            },
        )
    )
