from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TypeUnitOfMeasure:
    """
    Parameters
    ----------
    value
    unit
        Unit values would be lb,Lb,kg etc.
    """

    class Meta:
        name = "typeUnitOfMeasure"

    value: None | float = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
        },
    )
    unit: None | str = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Attribute",
        },
    )
