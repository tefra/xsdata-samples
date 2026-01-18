from __future__ import annotations

from dataclasses import dataclass

from .t_resource_assignment_expression import TResourceAssignmentExpression

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class ResourceAssignmentExpression(TResourceAssignmentExpression):
    class Meta:
        name = "resourceAssignmentExpression"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
