from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .taxi_stand import TaxiStand

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TaxiStandsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "taxiStands_RelStructure"

    taxi_stand: Iterable[TaxiStand] = field(
        default_factory=list,
        metadata={
            "name": "TaxiStand",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
