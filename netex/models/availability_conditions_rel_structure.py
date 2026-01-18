from collections.abc import Iterable
from dataclasses import dataclass, field

from .availability_condition_ref import AvailabilityConditionRef
from .containment_aggregation_structure import ContainmentAggregationStructure
from .entity_in_version_structure import (
    AvailabilityCondition,
    ValidBetween,
    ValidDuring,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AvailabilityConditionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "availabilityConditions_RelStructure"

    choice: Iterable[
        AvailabilityConditionRef
        | AvailabilityCondition
        | ValidDuring
        | ValidBetween
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AvailabilityConditionRef",
                    "type": AvailabilityConditionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AvailabilityCondition",
                    "type": AvailabilityCondition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidDuring",
                    "type": ValidDuring,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidBetween",
                    "type": ValidBetween,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
