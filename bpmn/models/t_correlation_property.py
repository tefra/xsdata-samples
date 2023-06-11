from dataclasses import dataclass, field
from typing import List, Optional
from xml.etree.ElementTree import QName
from .correlation_property_retrieval_expression import CorrelationPropertyRetrievalExpression
from .t_root_element import TRootElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TCorrelationProperty(TRootElement):
    class Meta:
        name = "tCorrelationProperty"

    correlation_property_retrieval_expression: List[CorrelationPropertyRetrievalExpression] = field(
        default_factory=list,
        metadata={
            "name": "correlationPropertyRetrievalExpression",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "min_occurs": 1,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type_value: Optional[QName] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        }
    )
