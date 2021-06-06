from dataclasses import dataclass
from .timing_point_version_structure import TimingPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingPoint1(TimingPointVersionStructure):
    class Meta:
        name = "TimingPoint"
        namespace = "http://www.netex.org.uk/netex"
