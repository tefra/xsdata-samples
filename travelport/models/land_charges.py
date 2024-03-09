from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.tax_1 import Tax1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class LandCharges:
    """
    Prints non-air charges on a document.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    tax: list[Tax1] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "max_occurs": 3,
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "name": "Base",
            "type": "Attribute",
        },
    )
    total: None | str = field(
        default=None,
        metadata={
            "name": "Total",
            "type": "Attribute",
        },
    )
    miscellaneous: None | str = field(
        default=None,
        metadata={
            "name": "Miscellaneous",
            "type": "Attribute",
        },
    )
    pre_paid: None | str = field(
        default=None,
        metadata={
            "name": "PrePaid",
            "type": "Attribute",
        },
    )
    deposit: None | str = field(
        default=None,
        metadata={
            "name": "Deposit",
            "type": "Attribute",
        },
    )
