from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class BrandId:
    """
    Brand ids for Merchandising details.
    """
    class Meta:
        name = "BrandID"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
        }
    )
