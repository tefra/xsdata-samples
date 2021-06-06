from dataclasses import dataclass
from .stop_event_request_ref_structure import StopEventRequestRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopEventRequestRef(StopEventRequestRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
