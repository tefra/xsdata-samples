from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.fare_display import FareDisplay

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirFareDisplayRsp(BaseRsp1):
    """
    Response to an AirFareDisplayReq.

    Parameters
    ----------
    fare_display
        Provider: 1G,1V,1P.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    fare_display: list[FareDisplay] = field(
        default_factory=list,
        metadata={
            "name": "FareDisplay",
            "type": "Element",
            "max_occurs": 999,
        },
    )
