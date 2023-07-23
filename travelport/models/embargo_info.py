from __future__ import annotations
from dataclasses import dataclass
from travelport.models.base_baggage_allowance_info import BaseBaggageAllowanceInfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class EmbargoInfo(BaseBaggageAllowanceInfo):
    """
    Information related to Embargo.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"
