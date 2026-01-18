from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class UnitedNations3:
    """
    United Nations Form of Payments.
    """

    class Meta:
        name = "UnitedNations"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    number: str = field(
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        }
    )
