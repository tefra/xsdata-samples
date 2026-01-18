from __future__ import annotations

from dataclasses import dataclass, field

from .common_vehicle_service_version_structure import (
    CommonVehicleServiceVersionStructure,
)
from .vehicle_pooling_ref import VehiclePoolingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehiclePoolingServiceVersionStructure(
    CommonVehicleServiceVersionStructure
):
    class Meta:
        name = "VehiclePoolingService_VersionStructure"

    vehicle_pooling_ref: VehiclePoolingRef | None = field(
        default=None,
        metadata={
            "name": "VehiclePoolingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    pooling_policy_url: str | None = field(
        default=None,
        metadata={
            "name": "PoolingPolicyUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
