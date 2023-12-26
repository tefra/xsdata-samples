from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class CabinClass6:
    """
    Requests cabin class (First, Business and Economy, etc.) as supported by the
    provider or supplier.
    """

    class Meta:
        name = "CabinClass"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
