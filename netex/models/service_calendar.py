from dataclasses import dataclass
from netex.models.service_calendar_version_structure import ServiceCalendarVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceCalendar(ServiceCalendarVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
