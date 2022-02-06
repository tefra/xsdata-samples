from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from .t_base_element import TBaseElement
from .t_formal_expression import TFormalExpression

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TCorrelationPropertyBinding(TBaseElement):
    class Meta:
        name = "tCorrelationPropertyBinding"

    data_path: Optional[TFormalExpression] = field(
        default=None,
        metadata={
            "name": "dataPath",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "required": True,
        }
    )
    correlation_property_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "correlationPropertyRef",
            "type": "Attribute",
            "required": True,
        }
    )
