from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from .common_vehicle_service_version_structure import (
    CommonVehicleServiceVersionStructure,
)
from .fleet_refs_rel_structure import FleetRefsRelStructure
from .vehicle_sharing_ref import VehicleSharingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleSharingServiceVersionStructure(
    CommonVehicleServiceVersionStructure
):
    class Meta:
        name = "VehicleSharingService_VersionStructure"

    vehicle_sharing_ref: Optional[VehicleSharingRef] = field(
        default=None,
        metadata={
            "name": "VehicleSharingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    sharing_policy_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "SharingPolicyUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_sharing_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumSharingPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_sharing_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumSharingPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    floating_vehicles: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FloatingVehicles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fleets: Optional[FleetRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
