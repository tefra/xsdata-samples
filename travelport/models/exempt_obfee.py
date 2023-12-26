from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class ExemptObfee:
    """
    Used to specify which OB fees are exempt; if none are listed, it means all
    should be exempt.
    """

    class Meta:
        name = "ExemptOBFee"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    sub_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "SubCode",
            "type": "Element",
            "max_occurs": 8,
        },
    )
