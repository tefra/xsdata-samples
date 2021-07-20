from dataclasses import dataclass, field
from typing import Optional
from .vehicle_access_facility_enumeration import VehicleAccessFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleAccessFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Optional[VehicleAccessFacilityEnumeration] = field(
        default=None
    )
