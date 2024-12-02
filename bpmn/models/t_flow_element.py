from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from .auditing import Auditing
from .monitoring import Monitoring
from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TFlowElement(TBaseElement):
    class Meta:
        name = "tFlowElement"

    auditing: Optional[Auditing] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    monitoring: Optional[Monitoring] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    category_value_ref: list[QName] = field(
        default_factory=list,
        metadata={
            "name": "categoryValueRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
