from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class NumberOfChildren:
    """
    Number of Children.

    Parameters
    ----------
    age
        The Ages of the Children. . The defined age of a Child traveler may
        vary by supplier, but is typically 1 to 17 years. Supported
        Providers 1G/1V.
    count
        The total number of children in the booking. Supported Providers 1P.
    amount
        Fee per child. Providers: 1g/1v
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    age: list[int] = field(
        default_factory=list,
        metadata={
            "name": "Age",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    count: None | int = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Attribute",
            "required": True,
        }
    )
    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
