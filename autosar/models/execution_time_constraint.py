from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .category_string import CategoryString
from .component_in_composition_instance_ref import (
    ComponentInCompositionInstanceRef,
)
from .executable_entity_subtypes_enum import ExecutableEntitySubtypesEnum
from .execution_time_type_enum import ExecutionTimeTypeEnum
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multidimensional_time import MultidimensionalTime
from .multilanguage_long_name import MultilanguageLongName
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .timing_condition_subtypes_enum import TimingConditionSubtypesEnum
from .traceable_subtypes_enum import TraceableSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class ExecutionTimeConstraint:
    """
    An ExecutionTimeConstraint is used to specify the execution time of the
    referenced ExecutableEntity in the referenced component.

    A minimum and maximum execution time can be defined. Two types of
    execution time semantics can be used. The desired semantics can be set
    by the attribute executionTimeType: * The "net" execution time is the
    time used to execute the ExecutableEntity without interruption and
    without external calls. * The "gross" execution time is the time used
    to execute the ExecutableEntity without interruption including external
    calls to other entities. The time to execute the ExecutableEntity
    including interruptions by other entities and including external calls
    is commonly called "response time". The TimingExtensions provide the
    concept of event chains and latency constraints for that purpose. An
    event chain from the start of the entity to the termination of the
    entity with according latency constraint represents a response time
    constraint for that executable entity.

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
    :ivar component_iref: The component that containts the referenced
        ExecutableEntity for the ExecutionTimeConstraint. If the entity
        is in a basic software module no component shall be provided.
    :ivar executable_ref: The referenced ExecutableEntity for the
        ExecutionTimeConstraint.
    :ivar execution_time_type: Specifies the type of the execution time
        constrained by ExecutionTimeConstraint,
    :ivar maximum: The maximum execution time.
    :ivar minimum: The minimum execution time.
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
        name = "EXECUTION-TIME-CONSTRAINT"

    short_name: Identifier = field(
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: None | ExecutionTimeConstraint.ShortNameFragments = (
        field(
            default=None,
            metadata={
                "name": "SHORT-NAME-FRAGMENTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    long_name: None | MultilanguageLongName = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: None | MultiLanguageOverviewParagraph = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: None | CategoryString = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: None | AdminData = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: None | DocumentationBlock = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: None | ExecutionTimeConstraint.Annotations = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    trace_refs: None | ExecutionTimeConstraint.TraceRefs = field(
        default=None,
        metadata={
            "name": "TRACE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timing_condition_ref: None | ExecutionTimeConstraint.TimingConditionRef = (
        field(
            default=None,
            metadata={
                "name": "TIMING-CONDITION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    variation_point: None | VariationPoint = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    component_iref: None | ComponentInCompositionInstanceRef = field(
        default=None,
        metadata={
            "name": "COMPONENT-IREF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    executable_ref: None | ExecutionTimeConstraint.ExecutableRef = field(
        default=None,
        metadata={
            "name": "EXECUTABLE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    execution_time_type: None | ExecutionTimeTypeEnum = field(
        default=None,
        metadata={
            "name": "EXECUTION-TIME-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    maximum: None | MultidimensionalTime = field(
        default=None,
        metadata={
            "name": "MAXIMUM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    minimum: None | MultidimensionalTime = field(
        default=None,
        metadata={
            "name": "MINIMUM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    uuid: None | str = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class ShortNameFragments:
        short_name_fragment: list[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class Annotations:
        annotation: list[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class TraceRefs:
        trace_ref: list[ExecutionTimeConstraint.TraceRefs.TraceRef] = field(
            default_factory=list,
            metadata={
                "name": "TRACE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass(kw_only=True)
        class TraceRef(Ref):
            dest: TraceableSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass(kw_only=True)
    class TimingConditionRef(Ref):
        dest: TimingConditionSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ExecutableRef(Ref):
        dest: ExecutableEntitySubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
