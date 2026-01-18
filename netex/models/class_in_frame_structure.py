from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .class_attribute_in_frame import ClassAttributeInFrame
from .class_ref_type_enumeration import ClassRefTypeEnumeration
from .class_relationship_in_frame import ClassRelationshipInFrame
from .mandatory_enumeration import MandatoryEnumeration
from .type_of_frame_ref import TypeOfFrameRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ClassInFrameStructure:
    class_ref_type: ClassRefTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "ClassRefType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_frame_ref: TypeOfFrameRef | None = field(
        default=None,
        metadata={
            "name": "TypeOfFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    mandatory: MandatoryEnumeration | None = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    attributes: ClassInFrameStructure.Attributes | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    relationships: ClassInFrameStructure.Relationships | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name_of_class: str | None = field(
        default=None,
        metadata={
            "name": "nameOfClass",
            "type": "Attribute",
        },
    )

    @dataclass
    class Attributes:
        class_attribute_in_frame: Iterable[ClassAttributeInFrame] = field(
            default_factory=list,
            metadata={
                "name": "ClassAttributeInFrame",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            },
        )

    @dataclass
    class Relationships:
        class_relationship_in_frame: Iterable[ClassRelationshipInFrame] = (
            field(
                default_factory=list,
                metadata={
                    "name": "ClassRelationshipInFrame",
                    "type": "Element",
                    "namespace": "http://www.netex.org.uk/netex",
                    "min_occurs": 1,
                },
            )
        )
