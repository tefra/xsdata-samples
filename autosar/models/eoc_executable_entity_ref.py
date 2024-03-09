from dataclasses import dataclass, field
from typing import List, Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from .bsw_implementation_subtypes_enum import BswImplementationSubtypesEnum
from .category_string import CategoryString
from .component_in_composition_instance_ref import (
    ComponentInCompositionInstanceRef,
)
from .eoc_executable_entity_ref_abstract_subtypes_enum import (
    EocExecutableEntityRefAbstractSubtypesEnum,
)
from .executable_entity_subtypes_enum import ExecutableEntitySubtypesEnum
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .ref import Ref
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EocExecutableEntityRef:
    """
    This is used to define a reference to an ExecutableEntity If the
    ExecutionOrderConstraint is defined on VFB, System or ECU level, a reference to
    the SwComponentPrototype, via the ComponentInCompositionInstanceRef, the
    referenced ExecutableEntity belongs to, shall be provided as context
    information.

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar long_name: This specifies the long name of the object. Long
        name is targeted to human readers and acts like a headline.
    :ivar desc: This represents a general but brief (one paragraph)
        description what the object in question is about. It is only one
        paragraph! Desc is intended to be collected into overview
        tables. This property helps a human reader to identify the
        object in question. More elaborate documentation, (in particular
        how the object is built or used) should go to "introduction".
    :ivar category: The category is a keyword that specializes the
        semantics of the Identifiable. It affects the expected existence
        of attributes and the applicability of constraints.
    :ivar admin_data: This represents the administrative data for the
        identifiable object.
    :ivar introduction: This represents more information about how the
        object in question is built or is used. Therefore it is a
        DocumentationBlock.
    :ivar annotations: Possibility to provide additional notes while
        defining a model element (e.g. the ECU Configuration Parameter
        Values). These are not intended as documentation but are mere
        design notes.
    :ivar direct_successor_refs: The direct successor of an executable
        entity or a group of executable entities.
    :ivar bsw_module_instance_ref: Specifies the BSW module instance the
        BSW module entity belongs to.
    :ivar component_iref: This association references the specific
        instance of the SW-C prototype.
    :ivar executable_ref: The ExecutableEntity whose execution order is
        restricted by the contraint.
    :ivar successor_refs: The logical successor of an executable entity
        or a group of executable entities.
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    :ivar uuid: The purpose of this attribute is to provide a globally
        unique identifier for an instance of a meta-class. The values of
        this attribute should be globally unique strings prefixed by the
        type of identifier.  For example, to include a DCE UUID as
        defined by The Open Group, the UUID would be preceded by "DCE:".
        The values of this attribute may be used to support merging of
        different AUTOSAR models. The form of the UUID (Universally
        Unique Identifier) is taken from a standard defined by the Open
        Group (was Open Software Foundation). This standard is widely
        used, including by Microsoft for COM (GUIDs) and by many
        companies for DCE, which is based on CORBA. The method for
        generating these 128-bit IDs is published in the standard and
        the effectiveness and uniqueness of the IDs is not in practice
        disputed. If the id namespace is omitted, DCE is assumed. An
        example is "DCE:2fac1234-31f8-11b4-a222-08002b34c003". The uuid
        attribute has no semantic meaning for an AUTOSAR model and there
        is no requirement for AUTOSAR tools to manage the timestamp.
    """

    class Meta:
        name = "EOC-EXECUTABLE-ENTITY-REF"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional[
        "EocExecutableEntityRef.ShortNameFragments"
    ] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: Optional[CategoryString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: Optional[AdminData] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: Optional["EocExecutableEntityRef.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    direct_successor_refs: Optional[
        "EocExecutableEntityRef.DirectSuccessorRefs"
    ] = field(
        default=None,
        metadata={
            "name": "DIRECT-SUCCESSOR-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    bsw_module_instance_ref: Optional[
        "EocExecutableEntityRef.BswModuleInstanceRef"
    ] = field(
        default=None,
        metadata={
            "name": "BSW-MODULE-INSTANCE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    component_iref: Optional[ComponentInCompositionInstanceRef] = field(
        default=None,
        metadata={
            "name": "COMPONENT-IREF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    executable_ref: Optional["EocExecutableEntityRef.ExecutableRef"] = field(
        default=None,
        metadata={
            "name": "EXECUTABLE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    successor_refs: Optional["EocExecutableEntityRef.SuccessorRefs"] = field(
        default=None,
        metadata={
            "name": "SUCCESSOR-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        },
    )

    @dataclass
    class ShortNameFragments:
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class DirectSuccessorRefs:
        direct_successor_ref: List[
            "EocExecutableEntityRef.DirectSuccessorRefs.DirectSuccessorRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIRECT-SUCCESSOR-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class DirectSuccessorRef(Ref):
            dest: Optional[EocExecutableEntityRefAbstractSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class BswModuleInstanceRef(Ref):
        dest: Optional[BswImplementationSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ExecutableRef(Ref):
        dest: Optional[ExecutableEntitySubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SuccessorRefs:
        successor_ref: List[
            "EocExecutableEntityRef.SuccessorRefs.SuccessorRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "SUCCESSOR-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class SuccessorRef(Ref):
            dest: Optional[EocExecutableEntityRefAbstractSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
