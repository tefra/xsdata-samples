from dataclasses import dataclass

from .fare_frame_version_frame_structure import FareFrameVersionFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareFrame(FareFrameVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
