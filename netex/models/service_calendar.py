from __future__ import annotations

from dataclasses import dataclass

from .service_calendar_version_structure import ServiceCalendarVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceCalendar(ServiceCalendarVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
