from __future__ import annotations

from dataclasses import dataclass

from .t_complex_gateway import TComplexGateway

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class ComplexGateway(TComplexGateway):
    class Meta:
        name = "complexGateway"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
