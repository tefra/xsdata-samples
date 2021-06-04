from dataclasses import dataclass, field
from typing import List
from netex.models.check_constraint import CheckConstraint
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CheckConstraintInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "checkConstraintInFrame_RelStructure"

    check_constraint: List[CheckConstraint] = field(
        default_factory=list,
        metadata={
            "name": "CheckConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
