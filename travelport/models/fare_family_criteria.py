from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class FareFamilyCriteria:
    """
    It is a branded Fare for a carrier and given fare basis code.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    carrier: str = field(
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    label: None | str = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 32,
        },
    )
    fare_basis: None | str = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
            "max_length": 20,
        },
    )
