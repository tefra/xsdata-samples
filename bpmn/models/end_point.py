from __future__ import annotations

from dataclasses import dataclass

from .t_end_point import TEndPoint

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class EndPoint(TEndPoint):
    class Meta:
        name = "endPoint"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
