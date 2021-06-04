from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.fare_point_in_pattern import FarePointInPattern
from netex.models.fare_point_in_pattern_ref import FarePointInPatternRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FarePointsInPatternRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "farePointsInPattern_RelStructure"

    fare_point_in_pattern_ref: List[FarePointInPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "FarePointInPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_point_in_pattern: List[FarePointInPattern] = field(
        default_factory=list,
        metadata={
            "name": "FarePointInPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
