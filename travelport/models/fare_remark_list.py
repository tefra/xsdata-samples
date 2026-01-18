from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.fare_remark import FareRemark

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class FareRemarkList:
    """
    The shared object list of FareInfos.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    fare_remark: list[FareRemark] = field(
        default_factory=list,
        metadata={
            "name": "FareRemark",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
