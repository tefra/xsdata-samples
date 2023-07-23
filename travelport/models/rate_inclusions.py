from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.included_item import IncludedItem

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class RateInclusions:
    """Provides the list of additional charges included in Rate.

    e.g Tax, Airport Surcharge, CDW etc
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    included_item: list[IncludedItem] = field(
        default_factory=list,
        metadata={
            "name": "IncludedItem",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
