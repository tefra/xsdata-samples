from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .category_string import CategoryString
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .ref import Ref
from .role_based_mc_data_assignment import RoleBasedMcDataAssignment
from .rpt_executable_entity_properties import RptExecutableEntityProperties
from .rpt_execution_context_subtypes_enum import (
    RptExecutionContextSubtypesEnum,
)
from .rpt_impl_policy import RptImplPolicy
from .rpt_service_point_subtypes_enum import RptServicePointSubtypesEnum
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RptExecutableEntityEvent:
    """
    This describes an ExecutableEntity event instance which can be bypassed.

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
    :ivar execution_context_refs: This describes the context in which
        the event of the executable entity is executed.
    :ivar mc_data_assignments: Reference to related McDataElements
        describing the implementation of „RP runnable disabler flag" and
        "stimulation enabler flag" The possible roles of the
        RoleBasedMcDataAssignment.role attribute are: *
        RpRunnableDisablerFlag"
    :ivar rpt_event_id: RPT event id used for service points call.
    :ivar rpt_executable_entity_properties: Describes the implemented
        code preparation for rapid prototyping at ExecutableEntity
        invocation.
    :ivar rpt_impl_policy: Describes the RptImplPolicy of a
        RptExecutableEvent for service based bypassing.
    :ivar rpt_service_point_post_refs: This describes the applicable
        Post Service Points for a RTEEvent / BswEvent of a bypassed
        ExecutableEntity.
    :ivar rpt_service_point_pre_refs: This describes the applicable Pre
        Service Points for a RTEEvent / BswEvent of a bypassed
        ExecutableEntity.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "RPT-EXECUTABLE-ENTITY-EVENT"

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
        "RptExecutableEntityEvent.ShortNameFragments"
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
    annotations: Optional["RptExecutableEntityEvent.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    execution_context_refs: Optional[
        "RptExecutableEntityEvent.ExecutionContextRefs"
    ] = field(
        default=None,
        metadata={
            "name": "EXECUTION-CONTEXT-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mc_data_assignments: Optional[
        "RptExecutableEntityEvent.McDataAssignments"
    ] = field(
        default=None,
        metadata={
            "name": "MC-DATA-ASSIGNMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rpt_event_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "RPT-EVENT-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rpt_executable_entity_properties: Optional[
        RptExecutableEntityProperties
    ] = field(
        default=None,
        metadata={
            "name": "RPT-EXECUTABLE-ENTITY-PROPERTIES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rpt_impl_policy: Optional[RptImplPolicy] = field(
        default=None,
        metadata={
            "name": "RPT-IMPL-POLICY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rpt_service_point_post_refs: Optional[
        "RptExecutableEntityEvent.RptServicePointPostRefs"
    ] = field(
        default=None,
        metadata={
            "name": "RPT-SERVICE-POINT-POST-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rpt_service_point_pre_refs: Optional[
        "RptExecutableEntityEvent.RptServicePointPreRefs"
    ] = field(
        default=None,
        metadata={
            "name": "RPT-SERVICE-POINT-PRE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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
    class ExecutionContextRefs:
        execution_context_ref: List[
            "RptExecutableEntityEvent.ExecutionContextRefs.ExecutionContextRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "EXECUTION-CONTEXT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ExecutionContextRef(Ref):
            dest: Optional[RptExecutionContextSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class McDataAssignments:
        role_based_mc_data_assignment: List[RoleBasedMcDataAssignment] = field(
            default_factory=list,
            metadata={
                "name": "ROLE-BASED-MC-DATA-ASSIGNMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class RptServicePointPostRefs:
        rpt_service_point_post_ref: List[
            "RptExecutableEntityEvent.RptServicePointPostRefs.RptServicePointPostRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "RPT-SERVICE-POINT-POST-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class RptServicePointPostRef(Ref):
            dest: Optional[RptServicePointSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class RptServicePointPreRefs:
        rpt_service_point_pre_ref: List[
            "RptExecutableEntityEvent.RptServicePointPreRefs.RptServicePointPreRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "RPT-SERVICE-POINT-PRE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class RptServicePointPreRef(Ref):
            dest: Optional[RptServicePointSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
