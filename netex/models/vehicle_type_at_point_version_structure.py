from __future__ import annotations

from dataclasses import dataclass, field

from .network_restriction_version_structure import (
    NetworkRestrictionVersionStructure,
)
from .transport_type_ref_structure import TransportTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleTypeAtPointVersionStructure(NetworkRestrictionVersionStructure):
    class Meta:
        name = "VehicleTypeAtPoint_VersionStructure"

    for_vehicle_type_ref: TransportTypeRefStructure | None = field(
        default=None,
        metadata={
            "name": "ForVehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    capacity: int | None = field(
        default=None,
        metadata={
            "name": "Capacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
