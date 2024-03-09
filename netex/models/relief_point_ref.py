from dataclasses import dataclass

from .relief_point_ref_structure import ReliefPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ReliefPointRef(ReliefPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
