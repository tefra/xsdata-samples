from dataclasses import dataclass, field
from typing import List
from netex.models.check_constraint import CheckConstraint
from netex.models.check_constraint_ref import CheckConstraintRef
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CheckConstraintsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "checkConstraints_RelStructure"

    check_constraint_ref: List[CheckConstraintRef] = field(
        default_factory=list,
        metadata={
            "name": "CheckConstraintRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    check_constraint: List[CheckConstraint] = field(
        default_factory=list,
        metadata={
            "name": "CheckConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
