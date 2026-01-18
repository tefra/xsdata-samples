from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.rail_solution_changed_info import (
    RailSolutionChangedInfo,
)
from travelport.models.universal_record import UniversalRecord

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class TypeRailCreateReservationRsp(BaseRsp1):
    class Meta:
        name = "typeRailCreateReservationRsp"

    universal_record: None | UniversalRecord = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/universal_v52_0",
        },
    )
    rail_solution_changed_info: list[RailSolutionChangedInfo] = field(
        default_factory=list,
        metadata={
            "name": "RailSolutionChangedInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
            "max_occurs": 999,
        },
    )
