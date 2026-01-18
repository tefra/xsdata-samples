from __future__ import annotations

from dataclasses import dataclass

from .vehicle_type_zone_restriction_version_structure import (
    VehicleTypeZoneRestrictionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleTypeZoneRestriction(VehicleTypeZoneRestrictionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
