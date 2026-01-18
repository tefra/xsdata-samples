from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .submode import Submode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SubmodesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "submodes_RelStructure"

    submode: Iterable[Submode] = field(
        default_factory=list,
        metadata={
            "name": "Submode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
