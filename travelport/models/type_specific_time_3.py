from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass(kw_only=True)
class TypeSpecificTime3:
    """
    Specify exact times.

    System will automatically convert to a range according to agency
    configuration.
    """

    class Meta:
        name = "typeSpecificTime"

    time: str = field(
        metadata={
            "name": "Time",
            "type": "Attribute",
            "required": True,
        }
    )
