from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.fare_info import FareInfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FareInfoList:
    """
    The shared object list of FareInfos.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    fare_info: list[FareInfo] = field(
        default_factory=list,
        metadata={
            "name": "FareInfo",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
