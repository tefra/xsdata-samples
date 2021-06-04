from dataclasses import dataclass, field
from typing import List
from netex.models.month_validity_offset import MonthValidityOffset
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MonthValidityOffsetsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "monthValidityOffsets_RelStructure"

    month_validity_offset: List[MonthValidityOffset] = field(
        default_factory=list,
        metadata={
            "name": "MonthValidityOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
