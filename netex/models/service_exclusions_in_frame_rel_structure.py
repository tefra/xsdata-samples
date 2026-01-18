from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .service_exclusion import ServiceExclusion

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceExclusionsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "serviceExclusionsInFrame_RelStructure"

    service_exclusion: Iterable[ServiceExclusion] = field(
        default_factory=list,
        metadata={
            "name": "ServiceExclusion",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
