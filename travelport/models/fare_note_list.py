from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.fare_note import FareNote

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FareNoteList:
    """
    The shared object list of Notes.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    fare_note: list[FareNote] = field(
        default_factory=list,
        metadata={
            "name": "FareNote",
            "type": "Element",
            "max_occurs": 999,
        },
    )
