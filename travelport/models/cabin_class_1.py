from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass(kw_only=True)
class CabinClass1:
    """
    Requests cabin class (First, Business and Economy, etc.) as supported
    by the provider or supplier.
    """

    class Meta:
        name = "CabinClass"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    type_value: str = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
