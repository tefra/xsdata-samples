from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .timeband import Timeband

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimebandsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "timebandsInFrame_RelStructure"

    timeband: Iterable[Timeband] = field(
        default_factory=list,
        metadata={
            "name": "Timeband",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
