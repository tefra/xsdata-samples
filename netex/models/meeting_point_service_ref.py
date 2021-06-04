from dataclasses import dataclass
from netex.models.meeting_point_service_ref_structure import MeetingPointServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MeetingPointServiceRef(MeetingPointServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
