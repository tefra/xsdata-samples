from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .boolean import Boolean
from .category_string import CategoryString
from .composition_sw_component_type_subtypes_enum import (
    CompositionSwComponentTypeSubtypesEnum,
)
from .eoc_event_ref import EocEventRef
from .eoc_executable_entity_ref import EocExecutableEntityRef
from .eoc_executable_entity_ref_group import EocExecutableEntityRefGroup
from .execution_order_constraint_type_enum import (
    ExecutionOrderConstraintTypeEnum,
)
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .timing_condition_subtypes_enum import TimingConditionSubtypesEnum
from .traceable_subtypes_enum import TraceableSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ExecutionOrderConstraint:
    """
    This constraint is used to restrict the order of execution for a set of
    ExecutableEntities.

    The ExecutionOrderConstraint can be used in any timing view. The
    various scopes for ExecutionOrderConstraint are described below.
    Generally, each ExecutionOrderConstraint has a scope of software
    components and can reference all executable entities available in the
    corresponding internal behavior (RunnableEntity and BswModuleEntity)
    either directly or by the events activating respectively starting them
    (RteEvent and BswEvent). On VFB level an ExecutionOrderConstraint can
    be specified for RunnableEntities part of the composition hierarchy
    referenced by the VfbTiming. The ExecutionOrderConstraint is aggregated
    by the VfbTiming. On SW-C level an ExecutionOrderConstraint can be
    specified for RunnableEntities part of the InternalBehavior referenced
    by the SwcTiming. The ExecutionOrderConstraint is aggregated by the
    SwcTiming. On System level an ExecutionOrderConstraint can be specified
    for RunnableEntities part of the composition hierarchy of the system
    referenced by the SystemTiming. The ExecutionOrderConstraint is
    aggregated by the SystemTiming. On BSW Module level, an
    ExectionOrderConstraint can be specified for BswModuleEntities part of
    an BswInternalBehavior referenced by the BswModuleTiming. The
    ExecutionOrderConstraint is aggregated by the BswModuleTiming. On ECU
    level an ExecutionOrderConstraint can be specified for all
    ExecutableEntities and Events available via the EcucValueCollection,
    covering ECU Extract and BSW Module Configuration, referenced by the
    EcuTiming. The ExecutionOrderConstraint is aggregated by the EcuTiming.

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
    :ivar trace_refs: This assocation represents the ability to trace to
        upstream requirements / constraints. This supports for example
        the bottom up tracing ProjectObjectives &lt;- MainRequirements
        &lt;- Features &lt;- RequirementSpecs &lt;- BSW/AI
    :ivar timing_condition_ref: A timing condition the timing constraint
        depends on. In other words it specifies the condition the timing
        constraint holds.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar base_composition_ref: Specifies the composition SW-C type
        playing the role of a SW-C containing further SW-Cs and
        represents the scope of the Execution Order Constraint.
    :ivar execution_order_constraint_type: Specifies the specific type
        of ExecutionOrderConstraint.
    :ivar ignore_order_allowed: Controls whether the order of execution
        specified by this constraint can be intentionally ignored
        (TRUE), or shall be respected (FALSE).
    :ivar is_event: Indicates whether the ExecutionOrderConstraint is
        only referring to Executable Entities (FALSE) or only to RTE
        and/or BSW Events (TRUE).
    :ivar ordered_elements: The list of references to ExecutableEntities
        which shall be ordered.
    :ivar permit_multiple_references_to_ee: Indicates that the
        ExecutionOrderConstraints permits that an Executable Entity is
        referenced multiple times (TRUE) or only once (FALSE) in the
        constraint.
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
        name = "EXECUTION-ORDER-CONSTRAINT"

    short_name: Identifier | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: ExecutionOrderConstraint.ShortNameFragments | None = field(
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
    annotations: ExecutionOrderConstraint.Annotations | None = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    trace_refs: ExecutionOrderConstraint.TraceRefs | None = field(
        default=None,
        metadata={
            "name": "TRACE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timing_condition_ref: ExecutionOrderConstraint.TimingConditionRef | None = field(
        default=None,
        metadata={
            "name": "TIMING-CONDITION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: VariationPoint | None = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    base_composition_ref: ExecutionOrderConstraint.BaseCompositionRef | None = field(
        default=None,
        metadata={
            "name": "BASE-COMPOSITION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    execution_order_constraint_type: ExecutionOrderConstraintTypeEnum | None = field(
        default=None,
        metadata={
            "name": "EXECUTION-ORDER-CONSTRAINT-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ignore_order_allowed: Boolean | None = field(
        default=None,
        metadata={
            "name": "IGNORE-ORDER-ALLOWED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    is_event: Boolean | None = field(
        default=None,
        metadata={
            "name": "IS-EVENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ordered_elements: ExecutionOrderConstraint.OrderedElements | None = (
        field(
            default=None,
            metadata={
                "name": "ORDERED-ELEMENTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    permit_multiple_references_to_ee: Boolean | None = field(
        default=None,
        metadata={
            "name": "PERMIT-MULTIPLE-REFERENCES-TO-EE",
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
    class TraceRefs:
        trace_ref: list[ExecutionOrderConstraint.TraceRefs.TraceRef] = field(
            default_factory=list,
            metadata={
                "name": "TRACE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class TraceRef(Ref):
            dest: TraceableSubtypesEnum | None = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class TimingConditionRef(Ref):
        dest: TimingConditionSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class BaseCompositionRef(Ref):
        dest: CompositionSwComponentTypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class OrderedElements:
        eoc_event_ref: list[EocEventRef] = field(
            default_factory=list,
            metadata={
                "name": "EOC-EVENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        eoc_executable_entity_ref: list[EocExecutableEntityRef] = field(
            default_factory=list,
            metadata={
                "name": "EOC-EXECUTABLE-ENTITY-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        eoc_executable_entity_ref_group: list[EocExecutableEntityRefGroup] = (
            field(
                default_factory=list,
                metadata={
                    "name": "EOC-EXECUTABLE-ENTITY-REF-GROUP",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
