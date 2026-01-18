from __future__ import annotations

from dataclasses import dataclass

from .service_calendar_frame_version_frame_structure import (
    ServiceCalendarFrameVersionFrameStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceCalendarFrame(ServiceCalendarFrameVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
