from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .duty import Duty

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DutiesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "dutiesInFrame_RelStructure"

    duty: Iterable[Duty] = field(
        default_factory=list,
        metadata={
            "name": "Duty",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
