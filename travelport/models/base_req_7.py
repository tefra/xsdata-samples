from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_core_req_7 import BaseCoreReq7
from travelport.models.override_pcc_7 import OverridePcc7

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass(kw_only=True)
class BaseReq7(BaseCoreReq7):
    class Meta:
        name = "BaseReq"

    override_pcc: None | OverridePcc7 = field(
        default=None,
        metadata={
            "name": "OverridePCC",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
        },
    )
    retrieve_provider_reservation_details: bool = field(
        default=False,
        metadata={
            "name": "RetrieveProviderReservationDetails",
            "type": "Attribute",
        },
    )
