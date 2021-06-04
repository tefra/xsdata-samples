from dataclasses import dataclass
from netex.models.service_calendar_ref_structure import ServiceCalendarRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceCalendarRef(ServiceCalendarRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
