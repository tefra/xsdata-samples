from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .age_constraint import AgeConstraint
from .arbitrary_event_triggering import ArbitraryEventTriggering
from .bsw_implementation_subtypes_enum import BswImplementationSubtypesEnum
from .burst_pattern_event_triggering import BurstPatternEventTriggering
from .category_string import CategoryString
from .concrete_pattern_event_triggering import ConcretePatternEventTriggering
from .execution_order_constraint import ExecutionOrderConstraint
from .execution_time_constraint import ExecutionTimeConstraint
from .identifier import Identifier
from .latency_timing_constraint import LatencyTimingConstraint
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .offset_timing_constraint import OffsetTimingConstraint
from .periodic_event_triggering import PeriodicEventTriggering
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .sporadic_event_triggering import SporadicEventTriggering
from .synchronization_point_constraint import SynchronizationPointConstraint
from .synchronization_timing_constraint import SynchronizationTimingConstraint
from .td_event_bsw_internal_behavior import TdEventBswInternalBehavior
from .td_event_bsw_mode_declaration import TdEventBswModeDeclaration
from .td_event_bsw_module import TdEventBswModule
from .td_event_complex import TdEventComplex
from .td_event_fr_cluster_cycle_start import TdEventFrClusterCycleStart
from .td_event_frame import TdEventFrame
from .td_event_frame_ethernet import TdEventFrameEthernet
from .td_event_i_pdu import TdEventIPdu
from .td_event_i_signal import TdEventISignal
from .td_event_mode_declaration import TdEventModeDeclaration
from .td_event_operation import TdEventOperation
from .td_event_service_instance_discovery import (
    TdEventServiceInstanceDiscovery,
)
from .td_event_service_instance_event import TdEventServiceInstanceEvent
from .td_event_service_instance_field import TdEventServiceInstanceField
from .td_event_service_instance_method import TdEventServiceInstanceMethod
from .td_event_swc_internal_behavior import TdEventSwcInternalBehavior
from .td_event_swc_internal_behavior_reference import (
    TdEventSwcInternalBehaviorReference,
)
from .td_event_trigger import TdEventTrigger
from .td_event_tt_can_cycle_start import TdEventTtCanCycleStart
from .td_event_variable_data_prototype import TdEventVariableDataPrototype
from .td_event_vfb_reference import TdEventVfbReference
from .timing_condition import TimingCondition
from .timing_description_event_chain import TimingDescriptionEventChain
from .timing_extension_resource import TimingExtensionResource

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BswCompositionTiming:
    """
    A model element used to define timing descriptions and constraints for
    a set of BswImplementations representing a BSW composition.

    A constraint defined at this level holds true for all referenced
    BswImplementations. Note, that multiple implementations of the same
    basic software module could be involved. TimingDescriptions aggregated
    by BswCompositionTiming are restricted to event chains referring to
    events which are derived from the class TDEventBswInternalBehavior and
    TDEventBsw.

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
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar timing_conditions: The timing condition specifies a specific
        condition. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar timing_descriptions: The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was -1.
    :ivar timing_guarantees: The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was -1.
    :ivar timing_requirements: The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was -1.
    :ivar timing_resource: The timing resource contains all instance
        references referred from within a timing condition formula of a
        timing view.
    :ivar implementation_refs: This defines the scope of a
        BswCompositionTiming. All corresponding timing descriptions and
        constraints shall be defined within this scope.
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
        name = "BSW-COMPOSITION-TIMING"

    short_name: None | Identifier = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: None | BswCompositionTiming.ShortNameFragments = (
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
    annotations: None | BswCompositionTiming.Annotations = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: None | VariationPoint = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timing_conditions: None | BswCompositionTiming.TimingConditions = field(
        default=None,
        metadata={
            "name": "TIMING-CONDITIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timing_descriptions: None | BswCompositionTiming.TimingDescriptions = (
        field(
            default=None,
            metadata={
                "name": "TIMING-DESCRIPTIONS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    timing_guarantees: None | BswCompositionTiming.TimingGuarantees = field(
        default=None,
        metadata={
            "name": "TIMING-GUARANTEES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timing_requirements: None | BswCompositionTiming.TimingRequirements = (
        field(
            default=None,
            metadata={
                "name": "TIMING-REQUIREMENTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    timing_resource: None | TimingExtensionResource = field(
        default=None,
        metadata={
            "name": "TIMING-RESOURCE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    implementation_refs: None | BswCompositionTiming.ImplementationRefs = (
        field(
            default=None,
            metadata={
                "name": "IMPLEMENTATION-REFS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
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
    class TimingConditions:
        timing_condition: list[TimingCondition] = field(
            default_factory=list,
            metadata={
                "name": "TIMING-CONDITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class TimingDescriptions:
        td_event_bsw_internal_behavior: list[TdEventBswInternalBehavior] = (
            field(
                default_factory=list,
                metadata={
                    "name": "TD-EVENT-BSW-INTERNAL-BEHAVIOR",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        td_event_bsw_mode_declaration: list[TdEventBswModeDeclaration] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-BSW-MODE-DECLARATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        td_event_bsw_module: list[TdEventBswModule] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-BSW-MODULE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        td_event_complex: list[TdEventComplex] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-COMPLEX",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        td_event_fr_cluster_cycle_start: list[TdEventFrClusterCycleStart] = (
            field(
                default_factory=list,
                metadata={
                    "name": "TD-EVENT-FR-CLUSTER-CYCLE-START",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        td_event_frame: list[TdEventFrame] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-FRAME",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        td_event_frame_ethernet: list[TdEventFrameEthernet] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-FRAME-ETHERNET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        td_event_i_pdu: list[TdEventIPdu] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-I-PDU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        td_event_i_signal: list[TdEventISignal] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-I-SIGNAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        td_event_mode_declaration: list[TdEventModeDeclaration] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-MODE-DECLARATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        td_event_operation: list[TdEventOperation] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-OPERATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        td_event_service_instance_discovery: list[
            TdEventServiceInstanceDiscovery
        ] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-SERVICE-INSTANCE-DISCOVERY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        td_event_service_instance_event: list[TdEventServiceInstanceEvent] = (
            field(
                default_factory=list,
                metadata={
                    "name": "TD-EVENT-SERVICE-INSTANCE-EVENT",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        td_event_service_instance_field: list[TdEventServiceInstanceField] = (
            field(
                default_factory=list,
                metadata={
                    "name": "TD-EVENT-SERVICE-INSTANCE-FIELD",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        td_event_service_instance_method: list[
            TdEventServiceInstanceMethod
        ] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-SERVICE-INSTANCE-METHOD",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        td_event_swc_internal_behavior: list[TdEventSwcInternalBehavior] = (
            field(
                default_factory=list,
                metadata={
                    "name": "TD-EVENT-SWC-INTERNAL-BEHAVIOR",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        td_event_swc_internal_behavior_reference: list[
            TdEventSwcInternalBehaviorReference
        ] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-SWC-INTERNAL-BEHAVIOR-REFERENCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        td_event_trigger: list[TdEventTrigger] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-TRIGGER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        td_event_tt_can_cycle_start: list[TdEventTtCanCycleStart] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-TT-CAN-CYCLE-START",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        td_event_variable_data_prototype: list[
            TdEventVariableDataPrototype
        ] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-VARIABLE-DATA-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        td_event_vfb_reference: list[TdEventVfbReference] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-VFB-REFERENCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        timing_description_event_chain: list[TimingDescriptionEventChain] = (
            field(
                default_factory=list,
                metadata={
                    "name": "TIMING-DESCRIPTION-EVENT-CHAIN",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )

    @dataclass
    class TimingGuarantees:
        age_constraint: list[AgeConstraint] = field(
            default_factory=list,
            metadata={
                "name": "AGE-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        arbitrary_event_triggering: list[ArbitraryEventTriggering] = field(
            default_factory=list,
            metadata={
                "name": "ARBITRARY-EVENT-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        burst_pattern_event_triggering: list[BurstPatternEventTriggering] = (
            field(
                default_factory=list,
                metadata={
                    "name": "BURST-PATTERN-EVENT-TRIGGERING",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        concrete_pattern_event_triggering: list[
            ConcretePatternEventTriggering
        ] = field(
            default_factory=list,
            metadata={
                "name": "CONCRETE-PATTERN-EVENT-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        execution_order_constraint: list[ExecutionOrderConstraint] = field(
            default_factory=list,
            metadata={
                "name": "EXECUTION-ORDER-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        execution_time_constraint: list[ExecutionTimeConstraint] = field(
            default_factory=list,
            metadata={
                "name": "EXECUTION-TIME-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        latency_timing_constraint: list[LatencyTimingConstraint] = field(
            default_factory=list,
            metadata={
                "name": "LATENCY-TIMING-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        offset_timing_constraint: list[OffsetTimingConstraint] = field(
            default_factory=list,
            metadata={
                "name": "OFFSET-TIMING-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        periodic_event_triggering: list[PeriodicEventTriggering] = field(
            default_factory=list,
            metadata={
                "name": "PERIODIC-EVENT-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        sporadic_event_triggering: list[SporadicEventTriggering] = field(
            default_factory=list,
            metadata={
                "name": "SPORADIC-EVENT-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        synchronization_point_constraint: list[
            SynchronizationPointConstraint
        ] = field(
            default_factory=list,
            metadata={
                "name": "SYNCHRONIZATION-POINT-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        synchronization_timing_constraint: list[
            SynchronizationTimingConstraint
        ] = field(
            default_factory=list,
            metadata={
                "name": "SYNCHRONIZATION-TIMING-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class TimingRequirements:
        age_constraint: list[AgeConstraint] = field(
            default_factory=list,
            metadata={
                "name": "AGE-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        arbitrary_event_triggering: list[ArbitraryEventTriggering] = field(
            default_factory=list,
            metadata={
                "name": "ARBITRARY-EVENT-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        burst_pattern_event_triggering: list[BurstPatternEventTriggering] = (
            field(
                default_factory=list,
                metadata={
                    "name": "BURST-PATTERN-EVENT-TRIGGERING",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        concrete_pattern_event_triggering: list[
            ConcretePatternEventTriggering
        ] = field(
            default_factory=list,
            metadata={
                "name": "CONCRETE-PATTERN-EVENT-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        execution_order_constraint: list[ExecutionOrderConstraint] = field(
            default_factory=list,
            metadata={
                "name": "EXECUTION-ORDER-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        execution_time_constraint: list[ExecutionTimeConstraint] = field(
            default_factory=list,
            metadata={
                "name": "EXECUTION-TIME-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        latency_timing_constraint: list[LatencyTimingConstraint] = field(
            default_factory=list,
            metadata={
                "name": "LATENCY-TIMING-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        offset_timing_constraint: list[OffsetTimingConstraint] = field(
            default_factory=list,
            metadata={
                "name": "OFFSET-TIMING-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        periodic_event_triggering: list[PeriodicEventTriggering] = field(
            default_factory=list,
            metadata={
                "name": "PERIODIC-EVENT-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        sporadic_event_triggering: list[SporadicEventTriggering] = field(
            default_factory=list,
            metadata={
                "name": "SPORADIC-EVENT-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        synchronization_point_constraint: list[
            SynchronizationPointConstraint
        ] = field(
            default_factory=list,
            metadata={
                "name": "SYNCHRONIZATION-POINT-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        synchronization_timing_constraint: list[
            SynchronizationTimingConstraint
        ] = field(
            default_factory=list,
            metadata={
                "name": "SYNCHRONIZATION-TIMING-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ImplementationRefs:
        implementation_ref: list[
            BswCompositionTiming.ImplementationRefs.ImplementationRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "IMPLEMENTATION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ImplementationRef(Ref):
            dest: None | BswImplementationSubtypesEnum = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
