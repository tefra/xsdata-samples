from dataclasses import dataclass

from .vehicle_meeting_place_version_structure import (
    VehicleMeetingPlaceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleMeetingPlace1(VehicleMeetingPlaceVersionStructure):
    class Meta:
        name = "VehicleMeetingPlace"
        namespace = "http://www.netex.org.uk/netex"
