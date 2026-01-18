from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class AdditionalInfo:
    """
    Parameters
    ----------
    category
        The category code is the code the AdditionalInfo text came from,
        e.g. S5 or S7.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    category: str = field(
        metadata={
            "name": "Category",
            "type": "Attribute",
            "required": True,
        }
    )
