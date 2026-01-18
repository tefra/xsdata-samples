from __future__ import annotations

from dataclasses import dataclass

from .vehicle_sharing_service_ref_structure import (
    VehicleSharingServiceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleSharingServiceRef(VehicleSharingServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
