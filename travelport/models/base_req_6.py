from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_core_req_6 import BaseCoreReq6
from travelport.models.override_pcc_6 import OverridePcc6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass(kw_only=True)
class BaseReq6(BaseCoreReq6):
    class Meta:
        name = "BaseReq"

    override_pcc: None | OverridePcc6 = field(
        default=None,
        metadata={
            "name": "OverridePCC",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v34_0",
        },
    )
    retrieve_provider_reservation_details: bool = field(
        default=False,
        metadata={
            "name": "RetrieveProviderReservationDetails",
            "type": "Attribute",
        },
    )
