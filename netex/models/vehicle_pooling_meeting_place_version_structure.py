from dataclasses import dataclass
from .vehicle_meeting_place_version_structure import (
    VehicleMeetingPlaceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehiclePoolingMeetingPlaceVersionStructure(
    VehicleMeetingPlaceVersionStructure
):
    class Meta:
        name = "VehiclePoolingMeetingPlace_VersionStructure"
