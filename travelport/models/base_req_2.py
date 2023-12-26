from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_core_req_2 import BaseCoreReq2
from travelport.models.override_pcc_2 import OverridePcc2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofileCommon_v30_0"


@dataclass
class BaseReq2(BaseCoreReq2):
    class Meta:
        name = "BaseReq"

    override_pcc: None | OverridePcc2 = field(
        default=None,
        metadata={
            "name": "OverridePCC",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
        },
    )
    retrieve_provider_reservation_details: bool = field(
        default=False,
        metadata={
            "name": "RetrieveProviderReservationDetails",
            "type": "Attribute",
        },
    )
