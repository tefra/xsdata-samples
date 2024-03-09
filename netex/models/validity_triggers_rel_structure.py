from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .entity_in_version_structure import ValidityTriggerVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ValidityTriggersRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "validityTriggers_RelStructure"

    validity_trigger: List[ValidityTriggerVersionStructure] = field(
        default_factory=list,
        metadata={
            "name": "ValidityTrigger",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
