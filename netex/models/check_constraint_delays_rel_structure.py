from dataclasses import dataclass, field
from typing import List
from netex.models.check_constraint_delay import CheckConstraintDelay
from netex.models.check_constraint_delay_ref import CheckConstraintDelayRef
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CheckConstraintDelaysRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "checkConstraintDelays_RelStructure"

    check_constraint_delay_ref: List[CheckConstraintDelayRef] = field(
        default_factory=list,
        metadata={
            "name": "CheckConstraintDelayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    check_constraint_delay: List[CheckConstraintDelay] = field(
        default_factory=list,
        metadata={
            "name": "CheckConstraintDelay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
