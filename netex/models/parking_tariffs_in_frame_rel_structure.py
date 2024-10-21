from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .parking_tariff import ParkingTariff

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingTariffsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "parkingTariffsInFrame_RelStructure"

    parking_tariff: Iterable[ParkingTariff] = field(
        default_factory=list,
        metadata={
            "name": "ParkingTariff",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
