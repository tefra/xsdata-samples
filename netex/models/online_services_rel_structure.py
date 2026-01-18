from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .online_service import OnlineService

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OnlineServicesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "onlineServices_RelStructure"

    online_service: Iterable[OnlineService] = field(
        default_factory=list,
        metadata={
            "name": "OnlineService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
