from dataclasses import dataclass
from .traffic_control_point_ref_structure import TrafficControlPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrafficControlPointRef(TrafficControlPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
