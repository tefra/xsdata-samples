from dataclasses import dataclass

from .driver_schedule_version_frame_structure import (
    DriverScheduleVersionFrameStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DriverScheduleFrame(DriverScheduleVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
