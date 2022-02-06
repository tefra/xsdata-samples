from dataclasses import dataclass
from .t_resource_assignment_expression import TResourceAssignmentExpression

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class ResourceAssignmentExpression(TResourceAssignmentExpression):
    class Meta:
        name = "resourceAssignmentExpression"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
