from dataclasses import dataclass

from .service_version_frame_structure import ServiceVersionFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceFrame(ServiceVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
