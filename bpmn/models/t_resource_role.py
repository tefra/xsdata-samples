from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .resource_assignment_expression import ResourceAssignmentExpression
from .resource_parameter_binding import ResourceParameterBinding
from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TResourceRole(TBaseElement):
    class Meta:
        name = "tResourceRole"

    resource_ref: None | QName = field(
        default=None,
        metadata={
            "name": "resourceRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    resource_parameter_binding: list[ResourceParameterBinding] = field(
        default_factory=list,
        metadata={
            "name": "resourceParameterBinding",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    resource_assignment_expression: None | ResourceAssignmentExpression = (
        field(
            default=None,
            metadata={
                "name": "resourceAssignmentExpression",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            },
        )
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
