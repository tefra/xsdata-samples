from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_segment import AirSegment
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.co2_emissions import Co2Emissions

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FlightDetailsRsp(BaseRsp1):
    """
    Parameters
    ----------
    air_segment
        Provider: 1G,1V,1P.
    co2_emissions
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment: list[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    co2_emissions: list[Co2Emissions] = field(
        default_factory=list,
        metadata={
            "name": "CO2Emissions",
            "type": "Element",
            "max_occurs": 99,
        }
    )
