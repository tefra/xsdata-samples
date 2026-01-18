from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .entity_in_version_structure import ValidityTriggerVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidityTriggersRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "validityTriggers_RelStructure"

    validity_trigger: Iterable[ValidityTriggerVersionStructure] = field(
        default_factory=list,
        metadata={
            "name": "ValidityTrigger",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
