from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .alternative_name import AlternativeName
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AlternativeNamesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "alternativeNames_RelStructure"

    alternative_name: Sequence[AlternativeName] = field(
        default_factory=list,
        metadata={
            "name": "AlternativeName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
