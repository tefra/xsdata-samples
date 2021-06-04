from dataclasses import dataclass
from netex.models.service_frame_ref_structure import ServiceFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceFrameRef(ServiceFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
