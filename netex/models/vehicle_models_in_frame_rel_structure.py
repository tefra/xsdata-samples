from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_model import VehicleModel

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleModelsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleModelsInFrame_RelStructure"

    vehicle_model: Iterable[VehicleModel] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
