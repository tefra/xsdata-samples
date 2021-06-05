from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.adaptive_platform_service_instance_subtypes_enum import AdaptivePlatformServiceInstanceSubtypesEnum
from autosar.models.age_constraint import AgeConstraint
from autosar.models.annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from autosar.models.arbitrary_event_triggering import ArbitraryEventTriggering
from autosar.models.burst_pattern_event_triggering import BurstPatternEventTriggering
from autosar.models.category_string import CategoryString
from autosar.models.concrete_pattern_event_triggering import ConcretePatternEventTriggering
from autosar.models.execution_order_constraint import ExecutionOrderConstraint
from autosar.models.execution_time_constraint import ExecutionTimeConstraint
from autosar.models.identifier import Identifier
from autosar.models.latency_timing_constraint import LatencyTimingConstraint
from autosar.models.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from autosar.models.multilanguage_long_name import MultilanguageLongName
from autosar.models.offset_timing_constraint import OffsetTimingConstraint
from autosar.models.periodic_event_triggering import PeriodicEventTriggering
from autosar.models.ref import Ref
from autosar.models.short_name_fragment import ShortNameFragment
from autosar.models.sporadic_event_triggering import SporadicEventTriggering
from autosar.models.synchronization_point_constraint import SynchronizationPointConstraint
from autosar.models.synchronization_timing_constraint import SynchronizationTimingConstraint
from autosar.models.td_event_bsw_internal_behavior import TdEventBswInternalBehavior
from autosar.models.td_event_bsw_mode_declaration import TdEventBswModeDeclaration
from autosar.models.td_event_bsw_module import TdEventBswModule
from autosar.models.td_event_complex import TdEventComplex
from autosar.models.td_event_fr_cluster_cycle_start import TdEventFrClusterCycleStart
from autosar.models.td_event_frame import TdEventFrame
from autosar.models.td_event_frame_ethernet import TdEventFrameEthernet
from autosar.models.td_event_i_pdu import TdEventIPdu
from autosar.models.td_event_i_signal import TdEventISignal
from autosar.models.td_event_mode_declaration import TdEventModeDeclaration
from autosar.models.td_event_operation import TdEventOperation
from autosar.models.td_event_service_instance_discovery import TdEventServiceInstanceDiscovery
from autosar.models.td_event_service_instance_event import TdEventServiceInstanceEvent
from autosar.models.td_event_service_instance_field import TdEventServiceInstanceField
from autosar.models.td_event_service_instance_method import TdEventServiceInstanceMethod
from autosar.models.td_event_swc_internal_behavior import TdEventSwcInternalBehavior
from autosar.models.td_event_swc_internal_behavior_reference import TdEventSwcInternalBehaviorReference
from autosar.models.td_event_trigger import TdEventTrigger
from autosar.models.td_event_tt_can_cycle_start import TdEventTtCanCycleStart
from autosar.models.td_event_variable_data_prototype import TdEventVariableDataPrototype
from autosar.models.td_event_vfb_reference import TdEventVfbReference
from autosar.models.timing_condition import TimingCondition
from autosar.models.timing_description_event_chain import TimingDescriptionEventChain
from autosar.models.timing_extension_resource import TimingExtensionResource

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ServiceTiming:
    """
    This meta-class represents the timing view for one or more service
    instances.

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
    :ivar service_instance_refs: This defines the scope of a
        ServiceTiming. All corresponding timing descriptions and
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
        name = "SERVICE-TIMING"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["ServiceTiming.ShortNameFragments"] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    long_name: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    category: Optional[CategoryString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    admin_data: Optional[AdminData] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    annotations: Optional["ServiceTiming.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    timing_conditions: Optional["ServiceTiming.TimingConditions"] = field(
        default=None,
        metadata={
            "name": "TIMING-CONDITIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    timing_descriptions: Optional["ServiceTiming.TimingDescriptions"] = field(
        default=None,
        metadata={
            "name": "TIMING-DESCRIPTIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    timing_guarantees: Optional["ServiceTiming.TimingGuarantees"] = field(
        default=None,
        metadata={
            "name": "TIMING-GUARANTEES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    timing_requirements: Optional["ServiceTiming.TimingRequirements"] = field(
        default=None,
        metadata={
            "name": "TIMING-REQUIREMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    timing_resource: Optional[TimingExtensionResource] = field(
        default=None,
        metadata={
            "name": "TIMING-RESOURCE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    service_instance_refs: Optional["ServiceTiming.ServiceInstanceRefs"] = field(
        default=None,
        metadata={
            "name": "SERVICE-INSTANCE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        }
    )

    @dataclass
    class ShortNameFragments:
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class TimingConditions:
        timing_condition: List[TimingCondition] = field(
            default_factory=list,
            metadata={
                "name": "TIMING-CONDITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class TimingDescriptions:
        td_event_bsw_internal_behavior: List[TdEventBswInternalBehavior] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-BSW-INTERNAL-BEHAVIOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        td_event_bsw_mode_declaration: List[TdEventBswModeDeclaration] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-BSW-MODE-DECLARATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        td_event_bsw_module: List[TdEventBswModule] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-BSW-MODULE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        td_event_complex: List[TdEventComplex] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-COMPLEX",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        td_event_fr_cluster_cycle_start: List[TdEventFrClusterCycleStart] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-FR-CLUSTER-CYCLE-START",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        td_event_frame: List[TdEventFrame] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-FRAME",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        td_event_frame_ethernet: List[TdEventFrameEthernet] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-FRAME-ETHERNET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        td_event_i_pdu: List[TdEventIPdu] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-I-PDU",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        td_event_i_signal: List[TdEventISignal] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-I-SIGNAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        td_event_mode_declaration: List[TdEventModeDeclaration] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-MODE-DECLARATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        td_event_operation: List[TdEventOperation] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-OPERATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        td_event_service_instance_discovery: List[TdEventServiceInstanceDiscovery] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-SERVICE-INSTANCE-DISCOVERY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        td_event_service_instance_event: List[TdEventServiceInstanceEvent] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-SERVICE-INSTANCE-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        td_event_service_instance_field: List[TdEventServiceInstanceField] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-SERVICE-INSTANCE-FIELD",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        td_event_service_instance_method: List[TdEventServiceInstanceMethod] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-SERVICE-INSTANCE-METHOD",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        td_event_swc_internal_behavior: List[TdEventSwcInternalBehavior] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-SWC-INTERNAL-BEHAVIOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        td_event_swc_internal_behavior_reference: List[TdEventSwcInternalBehaviorReference] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-SWC-INTERNAL-BEHAVIOR-REFERENCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        td_event_trigger: List[TdEventTrigger] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-TRIGGER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        td_event_tt_can_cycle_start: List[TdEventTtCanCycleStart] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-TT-CAN-CYCLE-START",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        td_event_variable_data_prototype: List[TdEventVariableDataPrototype] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-VARIABLE-DATA-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        td_event_vfb_reference: List[TdEventVfbReference] = field(
            default_factory=list,
            metadata={
                "name": "TD-EVENT-VFB-REFERENCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        timing_description_event_chain: List[TimingDescriptionEventChain] = field(
            default_factory=list,
            metadata={
                "name": "TIMING-DESCRIPTION-EVENT-CHAIN",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class TimingGuarantees:
        age_constraint: List[AgeConstraint] = field(
            default_factory=list,
            metadata={
                "name": "AGE-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        arbitrary_event_triggering: List[ArbitraryEventTriggering] = field(
            default_factory=list,
            metadata={
                "name": "ARBITRARY-EVENT-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        burst_pattern_event_triggering: List[BurstPatternEventTriggering] = field(
            default_factory=list,
            metadata={
                "name": "BURST-PATTERN-EVENT-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        concrete_pattern_event_triggering: List[ConcretePatternEventTriggering] = field(
            default_factory=list,
            metadata={
                "name": "CONCRETE-PATTERN-EVENT-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        execution_order_constraint: List[ExecutionOrderConstraint] = field(
            default_factory=list,
            metadata={
                "name": "EXECUTION-ORDER-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        execution_time_constraint: List[ExecutionTimeConstraint] = field(
            default_factory=list,
            metadata={
                "name": "EXECUTION-TIME-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        latency_timing_constraint: List[LatencyTimingConstraint] = field(
            default_factory=list,
            metadata={
                "name": "LATENCY-TIMING-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        offset_timing_constraint: List[OffsetTimingConstraint] = field(
            default_factory=list,
            metadata={
                "name": "OFFSET-TIMING-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        periodic_event_triggering: List[PeriodicEventTriggering] = field(
            default_factory=list,
            metadata={
                "name": "PERIODIC-EVENT-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        sporadic_event_triggering: List[SporadicEventTriggering] = field(
            default_factory=list,
            metadata={
                "name": "SPORADIC-EVENT-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        synchronization_point_constraint: List[SynchronizationPointConstraint] = field(
            default_factory=list,
            metadata={
                "name": "SYNCHRONIZATION-POINT-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        synchronization_timing_constraint: List[SynchronizationTimingConstraint] = field(
            default_factory=list,
            metadata={
                "name": "SYNCHRONIZATION-TIMING-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class TimingRequirements:
        age_constraint: List[AgeConstraint] = field(
            default_factory=list,
            metadata={
                "name": "AGE-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        arbitrary_event_triggering: List[ArbitraryEventTriggering] = field(
            default_factory=list,
            metadata={
                "name": "ARBITRARY-EVENT-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        burst_pattern_event_triggering: List[BurstPatternEventTriggering] = field(
            default_factory=list,
            metadata={
                "name": "BURST-PATTERN-EVENT-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        concrete_pattern_event_triggering: List[ConcretePatternEventTriggering] = field(
            default_factory=list,
            metadata={
                "name": "CONCRETE-PATTERN-EVENT-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        execution_order_constraint: List[ExecutionOrderConstraint] = field(
            default_factory=list,
            metadata={
                "name": "EXECUTION-ORDER-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        execution_time_constraint: List[ExecutionTimeConstraint] = field(
            default_factory=list,
            metadata={
                "name": "EXECUTION-TIME-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        latency_timing_constraint: List[LatencyTimingConstraint] = field(
            default_factory=list,
            metadata={
                "name": "LATENCY-TIMING-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        offset_timing_constraint: List[OffsetTimingConstraint] = field(
            default_factory=list,
            metadata={
                "name": "OFFSET-TIMING-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        periodic_event_triggering: List[PeriodicEventTriggering] = field(
            default_factory=list,
            metadata={
                "name": "PERIODIC-EVENT-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        sporadic_event_triggering: List[SporadicEventTriggering] = field(
            default_factory=list,
            metadata={
                "name": "SPORADIC-EVENT-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        synchronization_point_constraint: List[SynchronizationPointConstraint] = field(
            default_factory=list,
            metadata={
                "name": "SYNCHRONIZATION-POINT-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        synchronization_timing_constraint: List[SynchronizationTimingConstraint] = field(
            default_factory=list,
            metadata={
                "name": "SYNCHRONIZATION-TIMING-CONSTRAINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class ServiceInstanceRefs:
        service_instance_ref: List["ServiceTiming.ServiceInstanceRefs.ServiceInstanceRef"] = field(
            default_factory=list,
            metadata={
                "name": "SERVICE-INSTANCE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class ServiceInstanceRef(Ref):
            dest: Optional[AdaptivePlatformServiceInstanceSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )
