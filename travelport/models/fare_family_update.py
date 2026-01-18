from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.fare_family import FareFamily

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class FareFamilyUpdate:
    """
    Branded fare admin request element to Update a FareFamily.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    fare_family: FareFamily = field(
        metadata={
            "name": "FareFamily",
            "type": "Element",
            "required": True,
        }
    )
