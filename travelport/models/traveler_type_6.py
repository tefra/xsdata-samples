from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass(kw_only=True)
class TravelerType6:
    """
    The 3-char IATA traveler type code.
    """

    class Meta:
        name = "TravelerType"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    code: str = field(
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 3,
            "max_length": 5,
        }
    )
