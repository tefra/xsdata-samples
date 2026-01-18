from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .t_base_element import TBaseElement
from .t_relationship_direction import TRelationshipDirection

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TRelationship(TBaseElement):
    class Meta:
        name = "tRelationship"

    source: list[QName] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "min_occurs": 1,
        },
    )
    target: list[QName] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "min_occurs": 1,
        },
    )
    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
    direction: None | TRelationshipDirection = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
