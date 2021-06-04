from dataclasses import dataclass, field
from typing import List
from netex.models.alternative_texts_rel_structure import (
    AvailabilityCondition,
    ValidBetween,
    ValidDuring,
)
from netex.models.availability_condition_ref import AvailabilityConditionRef
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AvailabilityConditionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "availabilityConditions_RelStructure"

    availability_condition_ref: List[AvailabilityConditionRef] = field(
        default_factory=list,
        metadata={
            "name": "AvailabilityConditionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    availability_condition: List[AvailabilityCondition] = field(
        default_factory=list,
        metadata={
            "name": "AvailabilityCondition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    valid_during: List[ValidDuring] = field(
        default_factory=list,
        metadata={
            "name": "ValidDuring",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    valid_between: List[ValidBetween] = field(
        default_factory=list,
        metadata={
            "name": "ValidBetween",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
