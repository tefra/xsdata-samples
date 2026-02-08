from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
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

    language: str = field(
        metadata={
            "name": "Language",
            "type": "Attribute",
            "length": 2,
        }
    )
    country: str = field(
        metadata={
            "name": "Country",
            "type": "Attribute",
            "length": 2,
        }
    )
