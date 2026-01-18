from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class FareFamilyDelete:
    """
    Branded fare admin request element to delete a FareFamily for the given
    FareFamilyRef.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    fare_family_ref: str = field(
        metadata={
            "name": "FareFamilyRef",
            "type": "Attribute",
            "required": True,
        }
    )
    version: int = field(
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        }
    )
