from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Emdendorsement:
    """
    Endorsement for EMD.

    Supported providers are 1V/1G/1P.
    """

    class Meta:
        name = "EMDEndorsement"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 255,
        },
    )
