from dataclasses import dataclass

from .vehicle_schedule_version_frame_structure import (
    VehicleScheduleVersionFrameStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleScheduleFrame(VehicleScheduleVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
