from dataclasses import dataclass, field
from typing import List, Optional
from xml.etree.ElementTree import QName
from .t_base_element import TBaseElement
from .t_relationship_direction import TRelationshipDirection

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TRelationship(TBaseElement):
    class Meta:
        name = "tRelationship"

    source: List[QName] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "min_occurs": 1,
        },
    )
    target: List[QName] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "min_occurs": 1,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
    direction: Optional[TRelationshipDirection] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
