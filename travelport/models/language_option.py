from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class LanguageOption:
    """
    Enables itineraries and invoices to print in different languages.

    Parameters
    ----------
    language
        2 Letter ISO Language code
    country
        2 Letter ISO Country code
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    language: None | str = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Attribute",
            "required": True,
            "length": 2,
        },
    )
    country: None | str = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Attribute",
            "required": True,
            "length": 2,
        },
    )
