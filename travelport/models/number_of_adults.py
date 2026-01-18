from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass(kw_only=True)
class NumberOfAdults:
    """
    Number of Adults.

    Parameters
    ----------
    value
    extra_adults
        The number of extra adults in the room ,use '0' to delete the extra
        adults
    amount
        Fee for extra adults.  Providers: 1g/1v/1p
    content
        Additional information.  Providers 1p
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    extra_adults: None | int = field(
        default=None,
        metadata={
            "name": "ExtraAdults",
            "type": "Attribute",
        },
    )
    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        },
    )
    content: None | str = field(
        default=None,
        metadata={
            "name": "Content",
            "type": "Attribute",
        },
    )
