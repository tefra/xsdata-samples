from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_core_req_1 import BaseCoreReq1
from travelport.models.override_pcc_1 import OverridePcc1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class BaseReq1(BaseCoreReq1):
    class Meta:
        name = "BaseReq"

    override_pcc: None | OverridePcc1 = field(
        default=None,
        metadata={
            "name": "OverridePCC",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    retrieve_provider_reservation_details: bool = field(
        default=False,
        metadata={
            "name": "RetrieveProviderReservationDetails",
            "type": "Attribute",
        },
    )
