from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .t_base_element import TBaseElement
from .t_formal_expression import TFormalExpression

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TCorrelationPropertyBinding(TBaseElement):
    class Meta:
        name = "tCorrelationPropertyBinding"

    data_path: None | TFormalExpression = field(
        default=None,
        metadata={
            "name": "dataPath",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "required": True,
        },
    )
    correlation_property_ref: None | QName = field(
        default=None,
        metadata={
            "name": "correlationPropertyRef",
            "type": "Attribute",
            "required": True,
        },
    )
