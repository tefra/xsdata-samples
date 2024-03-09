from dataclasses import dataclass

from .timing_point_ref_structure import TimingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingPointRef(TimingPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
