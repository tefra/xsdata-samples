from dataclasses import dataclass

from .point_version_structure import PointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingPointAbstract(PointVersionStructure):
    class Meta:
        name = "TimingPoint_"
        namespace = "http://www.netex.org.uk/netex"
