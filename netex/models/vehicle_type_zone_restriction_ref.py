from dataclasses import dataclass

from .vehicle_type_zone_restriction_ref_structure import (
    VehicleTypeZoneRestrictionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleTypeZoneRestrictionRef(VehicleTypeZoneRestrictionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
