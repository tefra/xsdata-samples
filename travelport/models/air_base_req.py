from __future__ import annotations
from dataclasses import dataclass
from travelport.models.base_req_1 import BaseReq1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirBaseReq(BaseReq1):
    """
    Context for Requests and Responses.
    """
