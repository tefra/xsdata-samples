from __future__ import annotations

from dataclasses import dataclass

from .t_lane import TLaneSet

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class LaneSet(TLaneSet):
    class Meta:
        name = "laneSet"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
