from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_pooling_driver_info import VehiclePoolingDriverInfo

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePoolingDriverInfosRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehiclePoolingDriverInfos_RelStructure"

    vehicle_pooling_driver_info: Sequence[VehiclePoolingDriverInfo] = field(
        default_factory=list,
        metadata={
            "name": "VehiclePoolingDriverInfo",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
