from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/cruise_v52_0"


@dataclass(kw_only=True)
class CruiseFees:
    """
    Cruise Fees amount.

    Parameters
    ----------
    amount
        Total amount of fees associated for cruise
    description
        Text explaining fee amount
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    amount: str = field(
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 13,
        },
    )
