from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/cruise_v52_0"


@dataclass
class Commission3:
    """
    Cruise Commission.

    Parameters
    ----------
    amount
        Total amount of commission associated with cruise
    miscellaneous_amount
        Total amount of other Commission associated with cruise
    miscellaneous_description
        Text explaining other Commission amount
    """

    class Meta:
        name = "Commission"
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        },
    )
    miscellaneous_amount: None | str = field(
        default=None,
        metadata={
            "name": "MiscellaneousAmount",
            "type": "Attribute",
        },
    )
    miscellaneous_description: None | str = field(
        default=None,
        metadata={
            "name": "MiscellaneousDescription",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 13,
        },
    )
