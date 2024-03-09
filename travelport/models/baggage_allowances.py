from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.baggage_allowance_info import BaggageAllowanceInfo
from travelport.models.carry_on_allowance_info import CarryOnAllowanceInfo
from travelport.models.embargo_info import EmbargoInfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class BaggageAllowances:
    """
    Details of Baggage allowance.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    baggage_allowance_info: list[BaggageAllowanceInfo] = field(
        default_factory=list,
        metadata={
            "name": "BaggageAllowanceInfo",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    carry_on_allowance_info: list[CarryOnAllowanceInfo] = field(
        default_factory=list,
        metadata={
            "name": "CarryOnAllowanceInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    embargo_info: list[EmbargoInfo] = field(
        default_factory=list,
        metadata={
            "name": "EmbargoInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
