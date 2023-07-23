from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.flight_info import FlightInfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FlightInformationRsp(BaseRsp1):
    """
    Parameters
    ----------
    flight_info
        Provider: 1G,1V.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    flight_info: list[FlightInfo] = field(
        default_factory=list,
        metadata={
            "name": "FlightInfo",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
