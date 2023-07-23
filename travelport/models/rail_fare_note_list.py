from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.rail_fare_note import RailFareNote

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailFareNoteList:
    """
    The shared object list of Notes.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_fare_note: list[RailFareNote] = field(
        default_factory=list,
        metadata={
            "name": "RailFareNote",
            "type": "Element",
            "max_occurs": 999,
        }
    )
