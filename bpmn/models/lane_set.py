from dataclasses import dataclass
from .t_lane import TLaneSet

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class LaneSet(TLaneSet):
    class Meta:
        name = "laneSet"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
