from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class TravelerType2:
    """
    The 3-char IATA traveler type code.
    """

    class Meta:
        name = "TravelerType"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 3,
            "max_length": 5,
        },
    )
