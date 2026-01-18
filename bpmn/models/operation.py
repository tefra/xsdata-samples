from __future__ import annotations

from dataclasses import dataclass

from .t_operation import TOperation

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Operation(TOperation):
    class Meta:
        name = "operation"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
