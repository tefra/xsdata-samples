from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.characteristic_3 import Characteristic3
from travelport.models.facility import Facility

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Row:
    """
    Identifies the row of in a seat map.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    facility: list[Facility] = field(
        default_factory=list,
        metadata={
            "name": "Facility",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    characteristic: list[Characteristic3] = field(
        default_factory=list,
        metadata={
            "name": "Characteristic",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    number: None | int = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        }
    )
    search_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "SearchTravelerRef",
            "type": "Attribute",
        }
    )
