from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass(kw_only=True)
class TypeGuestChildInformation:
    """
    Infomration about the Child guest.

    Parameters
    ----------
    age
        Age of the Child.
    """

    class Meta:
        name = "typeGuestChildInformation"

    age: None | int = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Attribute",
        },
    )
