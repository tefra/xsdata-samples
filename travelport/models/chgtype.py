from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.pen_fee_type import PenFeeType

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Chgtype:
    """
    PenFee list will be populated.
    """

    class Meta:
        name = "CHGType"

    pen_fee: list[PenFeeType] = field(
        default_factory=list,
        metadata={
            "name": "PenFee",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 2,
        },
    )
