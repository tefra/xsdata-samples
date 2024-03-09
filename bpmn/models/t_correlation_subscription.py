from dataclasses import dataclass, field
from typing import List, Optional
from xml.etree.ElementTree import QName

from .correlation_property_binding import CorrelationPropertyBinding
from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TCorrelationSubscription(TBaseElement):
    class Meta:
        name = "tCorrelationSubscription"

    correlation_property_binding: List[CorrelationPropertyBinding] = field(
        default_factory=list,
        metadata={
            "name": "correlationPropertyBinding",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    correlation_key_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "correlationKeyRef",
            "type": "Attribute",
            "required": True,
        },
    )
