from dataclasses import dataclass
from netex.models.schedule_request_ref_structure import ScheduleRequestRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ScheduleRequestRef(ScheduleRequestRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
