from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from .class_ref_structure import ClassRefStructure
from .classes_in_repository_rel_structure import (
    ClassesInRepositoryRelStructure,
)
from .layer_ref import LayerRef
from .modification_set_enumeration import ModificationSetEnumeration
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_entity_refs_rel_structure import TypeOfEntityRefsRelStructure
from .type_of_entity_version_structure import TypeOfEntityVersionStructure
from .type_of_frame_ref import TypeOfFrameRef
from .type_of_validity_ref import TypeOfValidityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypesOfFrameRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typesOfFrame_RelStructure"

    type_of_frame_ref_or_type_of_frame: List[
        Union[TypeOfFrameRef, "TypeOfFrame"]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfFrameRef",
                    "type": TypeOfFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFrame",
                    "type": ForwardRef("TypeOfFrame"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass
class TypeOfFrameValueStructure(TypeOfEntityVersionStructure):
    class Meta:
        name = "TypeOfFrame_ValueStructure"

    type_of_validity_ref: Optional[TypeOfValidityRef] = field(
        default=None,
        metadata={
            "name": "TypeOfValidityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    frame_class_ref: Optional[ClassRefStructure] = field(
        default=None,
        metadata={
            "name": "FrameClassRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    classes: Optional[ClassesInRepositoryRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    types_of_entity: Optional[TypeOfEntityRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "typesOfEntity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    includes: Optional[TypesOfFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    locating_system_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatingSystemRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    modification_set: Optional[ModificationSetEnumeration] = field(
        default=None,
        metadata={
            "name": "ModificationSet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    layer_ref: Optional[LayerRef] = field(
        default=None,
        metadata={
            "name": "LayerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass
class TypeOfFrame(TypeOfFrameValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    name_of_classified_entity_class: str = field(
        init=False,
        default="VersionFrame",
        metadata={
            "name": "nameOfClassifiedEntityClass",
            "type": "Attribute",
        },
    )
