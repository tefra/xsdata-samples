from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .entity_in_version_structure import AvailabilityCondition

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ContainedAvailabilityConditionsRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "containedAvailabilityConditions_RelStructure"

    availability_condition: Sequence[AvailabilityCondition] = field(
        default_factory=list,
        metadata={
            "name": "AvailabilityCondition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
