from dataclasses import dataclass, field
from typing import Optional
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

    vehicle_pooling_ref: Optional[VehiclePoolingRef] = field(
        default=None,
        metadata={
            "name": "VehiclePoolingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    pooling_policy_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "PoolingPolicyUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
