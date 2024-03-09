from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_core_req_4 import BaseCoreReq4
from travelport.models.override_pcc_4 import OverridePcc4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class BaseReq4(BaseCoreReq4):
    class Meta:
        name = "BaseReq"

    override_pcc: None | OverridePcc4 = field(
        default=None,
        metadata={
            "name": "OverridePCC",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
        },
    )
    retrieve_provider_reservation_details: bool = field(
        default=False,
        metadata={
            "name": "RetrieveProviderReservationDetails",
            "type": "Attribute",
        },
    )
