from dataclasses import dataclass
from .vehicle_pooling_meeting_place_version_structure import (
    VehiclePoolingMeetingPlaceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehiclePoolingMeetingPlace(VehiclePoolingMeetingPlaceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
