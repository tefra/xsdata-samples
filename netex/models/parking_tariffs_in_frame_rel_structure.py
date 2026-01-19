from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .parking_tariff import ParkingTariff

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingTariffsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "parkingTariffsInFrame_RelStructure"

    parking_tariff: Sequence[ParkingTariff] = field(
        default_factory=list,
        metadata={
            "name": "ParkingTariff",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
