from dataclasses import dataclass

from .vehicle_meeting_point_ref_structure import (
    VehicleMeetingPointRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleMeetingPointRef(VehicleMeetingPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
