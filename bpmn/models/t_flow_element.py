from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .auditing import Auditing
from .monitoring import Monitoring
from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TFlowElement(TBaseElement):
    class Meta:
        name = "tFlowElement"

    auditing: None | Auditing = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    monitoring: None | Monitoring = field(
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
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
