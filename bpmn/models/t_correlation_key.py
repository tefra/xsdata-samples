from dataclasses import dataclass, field
from typing import List, Optional
from xml.etree.ElementTree import QName

from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TCorrelationKey(TBaseElement):
    class Meta:
        name = "tCorrelationKey"

    correlation_property_ref: List[QName] = field(
        default_factory=list,
        metadata={
            "name": "correlationPropertyRef",
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
