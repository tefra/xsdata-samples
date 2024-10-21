from collections.abc import Iterable
from dataclasses import dataclass, field

from .alternative_name import AlternativeName
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AlternativeNamesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "alternativeNames_RelStructure"

    alternative_name: Iterable[AlternativeName] = field(
        default_factory=list,
        metadata={
            "name": "AlternativeName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
