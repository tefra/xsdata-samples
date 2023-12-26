from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_core_req_3 import BaseCoreReq3
from travelport.models.override_pcc_3 import OverridePcc3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class BaseReq3(BaseCoreReq3):
    class Meta:
        name = "BaseReq"

    override_pcc: None | OverridePcc3 = field(
        default=None,
        metadata={
            "name": "OverridePCC",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
        },
    )
    retrieve_provider_reservation_details: bool = field(
        default=False,
        metadata={
            "name": "RetrieveProviderReservationDetails",
            "type": "Attribute",
        },
    )
