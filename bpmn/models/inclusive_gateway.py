from __future__ import annotations

from dataclasses import dataclass

from .t_inclusive_gateway import TInclusiveGateway

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class InclusiveGateway(TInclusiveGateway):
    class Meta:
        name = "inclusiveGateway"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
