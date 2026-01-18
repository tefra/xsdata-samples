from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass(kw_only=True)
class IncludedItem:
    """
    Provides details of included item.

    Parameters
    ----------
    code
        Code for included item.
    description
        Description of included item.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    code: str = field(
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
    description: str = field(
        metadata={
            "name": "Description",
            "type": "Attribute",
            "required": True,
        }
    )
