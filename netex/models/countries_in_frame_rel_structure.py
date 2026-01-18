from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .country import Country

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CountriesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "countriesInFrame_RelStructure"

    country: Iterable[Country] = field(
        default_factory=list,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
