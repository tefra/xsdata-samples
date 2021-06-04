from dataclasses import dataclass
from netex.models.service_calendar_frame_version_frame_structure import ServiceCalendarFrameVersionFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceCalendarFrame(ServiceCalendarFrameVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
