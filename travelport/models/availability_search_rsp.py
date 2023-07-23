from __future__ import annotations
from dataclasses import dataclass
from travelport.models.base_availability_search_rsp import BaseAvailabilitySearchRsp

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AvailabilitySearchRsp(BaseAvailabilitySearchRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"
