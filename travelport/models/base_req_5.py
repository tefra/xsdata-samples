from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_core_req_5 import BaseCoreReq5
from travelport.models.override_pcc_5 import OverridePcc5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class BaseReq5(BaseCoreReq5):
    class Meta:
        name = "BaseReq"

    override_pcc: None | OverridePcc5 = field(
        default=None,
        metadata={
            "name": "OverridePCC",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    retrieve_provider_reservation_details: bool = field(
        default=False,
        metadata={
            "name": "RetrieveProviderReservationDetails",
            "type": "Attribute",
        },
    )
