from dataclasses import dataclass
from .stop_finder_request_ref_structure import StopFinderRequestRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopFinderRequestRef(StopFinderRequestRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
