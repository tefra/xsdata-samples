from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .property_of_day import PropertyOfDay
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PropertiesOfDayRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "propertiesOfDay_RelStructure"

    property_of_day: Sequence[PropertyOfDay] = field(
        default_factory=list,
        metadata={
            "name": "PropertyOfDay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
