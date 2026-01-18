from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .flexible_point_properties import FlexiblePointProperties

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexiblePointPropertiesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "flexiblePointProperties_RelStructure"

    flexible_point_properties: Iterable[FlexiblePointProperties] = field(
        default_factory=list,
        metadata={
            "name": "FlexiblePointProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
