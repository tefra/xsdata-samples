from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass(kw_only=True)
class RailFareNoteRef:
    """
    A reference to a fare note from a shared list.

    Used to minimize xml results.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
