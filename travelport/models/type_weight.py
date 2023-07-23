from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_unit_weight import TypeUnitWeight

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TypeWeight:
    class Meta:
        name = "typeWeight"

    value: None | int = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
        }
    )
    unit: None | TypeUnitWeight = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Attribute",
        }
    )
