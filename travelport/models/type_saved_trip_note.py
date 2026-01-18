from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class TypeSavedTripNote:
    """
    Parameters
    ----------
    text
        Custom free Text related to SavedTrip.
    """

    class Meta:
        name = "typeSavedTripNote"

    text: str = field(
        metadata={
            "name": "Text",
            "type": "Attribute",
            "required": True,
            "max_length": 333,
        }
    )
