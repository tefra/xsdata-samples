from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .medium_application_instance import MediumApplicationInstance

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MediumApplicationInstanceRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "mediumApplicationInstance_RelStructure"

    medium_application_instance: Sequence[MediumApplicationInstance] = field(
        default_factory=list,
        metadata={
            "name": "MediumApplicationInstance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
