from dataclasses import dataclass

from .vehicle_meeting_point_version_structure import (
    VehicleMeetingPointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleMeetingPoint(VehicleMeetingPointVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
