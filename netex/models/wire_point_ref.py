from dataclasses import dataclass
from .wire_point_ref_structure import WirePointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class WirePointRef(WirePointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
