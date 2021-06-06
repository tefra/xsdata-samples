from dataclasses import dataclass, field
from typing import List
from .accommodation import Accommodation
from .accommodation_ref import AccommodationRef
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccommodationsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "accommodations_RelStructure"

    accommodation_ref: List[AccommodationRef] = field(
        default_factory=list,
        metadata={
            "name": "AccommodationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accommodation: List[Accommodation] = field(
        default_factory=list,
        metadata={
            "name": "Accommodation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
