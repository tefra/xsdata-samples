from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from .category_string import CategoryString
from .eoc_executable_entity_ref_abstract_subtypes_enum import (
    EocExecutableEntityRefAbstractSubtypesEnum,
)
from .identifier import Identifier
from .integer import Integer
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .timing_description_event_chain_subtypes_enum import (
    TimingDescriptionEventChainSubtypesEnum,
)
from .timing_description_event_subtypes_enum import (
    TimingDescriptionEventSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EocExecutableEntityRefGroup:
    """
    This is used to specify a group (composite) consisting of Execution
    Order Constraint Executable Entity References (leaves) and/or further
    Execution Order Constraint Executable Entity Reference Groups
    (composite).

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
    :ivar let_interval_refs: This association references the
        TimingDescriptionEventChain that plays the role of a LET
        interval the executable entities in the group are assigned to.
    :ivar max_cycles: In case of a Repetitive Execution Order Constraint
        this attribute specifies the number of cycles the Execution
        Order Constraint is considering.
    :ivar max_slots: In case of a Repetitive Execution Order Constraint
        this attribute specifies the number of slots every cycle of the
        Execution Order Constraint is consisting of.
    :ivar nested_element_refs: This association is used to establish
        hierarchies of EOCEER Groups and References.
    :ivar successor_refs: The logical successor of an executable entity
        or a group of executable entities.
    :ivar triggering_event_ref: In case of a Repetitive Execution Order
        Constraint this association references the timing description
        event triggering every cycle.
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
        name = "EOC-EXECUTABLE-ENTITY-REF-GROUP"

    short_name: Identifier | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: EocExecutableEntityRefGroup.ShortNameFragments | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: MultilanguageLongName | None = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: MultiLanguageOverviewParagraph | None = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: CategoryString | None = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: AdminData | None = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: DocumentationBlock | None = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: EocExecutableEntityRefGroup.Annotations | None = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    direct_successor_refs: EocExecutableEntityRefGroup.DirectSuccessorRefs | None = field(
        default=None,
        metadata={
            "name": "DIRECT-SUCCESSOR-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    let_interval_refs: EocExecutableEntityRefGroup.LetIntervalRefs | None = field(
        default=None,
        metadata={
            "name": "LET-INTERVAL-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_cycles: Integer | None = field(
        default=None,
        metadata={
            "name": "MAX-CYCLES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_slots: Integer | None = field(
        default=None,
        metadata={
            "name": "MAX-SLOTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nested_element_refs: EocExecutableEntityRefGroup.NestedElementRefs | None = field(
        default=None,
        metadata={
            "name": "NESTED-ELEMENT-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    successor_refs: EocExecutableEntityRefGroup.SuccessorRefs | None = (
        field(
            default=None,
            metadata={
                "name": "SUCCESSOR-REFS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    triggering_event_ref: EocExecutableEntityRefGroup.TriggeringEventRef | None = field(
        default=None,
        metadata={
            "name": "TRIGGERING-EVENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    uuid: str | None = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        },
    )

    @dataclass
    class ShortNameFragments:
        short_name_fragment: list[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Annotations:
        annotation: list[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class DirectSuccessorRefs:
        direct_successor_ref: list[
            EocExecutableEntityRefGroup.DirectSuccessorRefs.DirectSuccessorRef
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
            dest: EocExecutableEntityRefAbstractSubtypesEnum | None = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class LetIntervalRefs:
        let_interval_ref: list[
            EocExecutableEntityRefGroup.LetIntervalRefs.LetIntervalRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "LET-INTERVAL-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class LetIntervalRef(Ref):
            dest: TimingDescriptionEventChainSubtypesEnum | None = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class NestedElementRefs:
        nested_element_ref: list[
            EocExecutableEntityRefGroup.NestedElementRefs.NestedElementRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "NESTED-ELEMENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class NestedElementRef(Ref):
            dest: EocExecutableEntityRefAbstractSubtypesEnum | None = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class SuccessorRefs:
        successor_ref: list[
            EocExecutableEntityRefGroup.SuccessorRefs.SuccessorRef
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
            dest: EocExecutableEntityRefAbstractSubtypesEnum | None = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class TriggeringEventRef(Ref):
        dest: TimingDescriptionEventSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
