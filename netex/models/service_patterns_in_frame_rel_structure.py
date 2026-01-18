from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .service_pattern import ServicePattern

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServicePatternsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "servicePatternsInFrame_RelStructure"

    service_pattern: Iterable[ServicePattern] = field(
        default_factory=list,
        metadata={
            "name": "ServicePattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
