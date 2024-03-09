from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.universal_record import UniversalRecord

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class VehicleCancelRsp(BaseRsp1):
    """Response to a VehicleCancelReq.

    PNR returned reflects the requested modifications.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record: None | UniversalRecord = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
        },
    )
