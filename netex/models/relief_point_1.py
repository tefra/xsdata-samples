from dataclasses import dataclass
from netex.models.timing_point_version_structure import TimingPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ReliefPoint1(TimingPointVersionStructure):
    class Meta:
        name = "ReliefPoint_"
        namespace = "http://www.netex.org.uk/netex"
