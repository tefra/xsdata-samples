from __future__ import annotations

from dataclasses import dataclass

from .t_complex_behavior_definition import TComplexBehaviorDefinition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class ComplexBehaviorDefinition(TComplexBehaviorDefinition):
    class Meta:
        name = "complexBehaviorDefinition"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
