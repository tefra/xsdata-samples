from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from .bsw_asynchronous_server_call_returns_event import (
    BswAsynchronousServerCallReturnsEvent,
)
from .bsw_background_event import BswBackgroundEvent
from .bsw_called_entity import BswCalledEntity
from .bsw_client_policy import BswClientPolicy
from .bsw_data_received_event import BswDataReceivedEvent
from .bsw_data_send_policy import BswDataSendPolicy
from .bsw_distinguished_partition import BswDistinguishedPartition
from .bsw_exclusive_area_policy import BswExclusiveAreaPolicy
from .bsw_external_trigger_occurred_event import (
    BswExternalTriggerOccurredEvent,
)
from .bsw_internal_trigger_occurred_event import (
    BswInternalTriggerOccurredEvent,
)
from .bsw_internal_triggering_point import BswInternalTriggeringPoint
from .bsw_internal_triggering_point_policy import (
    BswInternalTriggeringPointPolicy,
)
from .bsw_interrupt_entity import BswInterruptEntity
from .bsw_mode_manager_error_event import BswModeManagerErrorEvent
from .bsw_mode_receiver_policy import BswModeReceiverPolicy
from .bsw_mode_sender_policy import BswModeSenderPolicy
from .bsw_mode_switch_event import BswModeSwitchEvent
from .bsw_mode_switched_ack_event import BswModeSwitchedAckEvent
from .bsw_operation_invoked_event import BswOperationInvokedEvent
from .bsw_os_task_execution_event import BswOsTaskExecutionEvent
from .bsw_parameter_policy import BswParameterPolicy
from .bsw_per_instance_memory_policy import BswPerInstanceMemoryPolicy
from .bsw_queued_data_reception_policy import BswQueuedDataReceptionPolicy
from .bsw_released_trigger_policy import BswReleasedTriggerPolicy
from .bsw_schedulable_entity import BswSchedulableEntity
from .bsw_scheduler_name_prefix import BswSchedulerNamePrefix
from .bsw_service_dependency import BswServiceDependency
from .bsw_timing_event import BswTimingEvent
from .bsw_trigger_direct_implementation import BswTriggerDirectImplementation
from .category_string import CategoryString
from .constant_specification_mapping_set_subtypes_enum import (
    ConstantSpecificationMappingSetSubtypesEnum,
)
from .data_type_mapping_set_subtypes_enum import DataTypeMappingSetSubtypesEnum
from .exclusive_area import ExclusiveArea
from .exclusive_area_nesting_order import ExclusiveAreaNestingOrder
from .identifier import Identifier
from .included_data_type_set import IncludedDataTypeSet
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .parameter_data_prototype import ParameterDataPrototype
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .variable_data_prototype import VariableDataPrototype
from .variation_point_proxy import VariationPointProxy

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class BswInternalBehavior:
    """
    Specifies the behavior of a BSW module or a BSW cluster w.r.t. the code
    entities visible by the BSW Scheduler.

    It is possible to have several different BswInternalBehaviors referring
    to the same BswModuleDescription.

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
    :ivar constant_memorys: Describes a read only memory object
        containing characteristic value(s)  implemented by this
        InternalBehavior. The shortName of ParameterDataPrototype has to
        be equal to the ''C' identifier of the described constant. The
        characteristic value(s) might be shared between
        SwComponentPrototypes of the same SwComponentType. The
        aggregation of constantMemory is subject to variability with the
        purpose to support variability in the software component or
        module implementations. Typically different algorithms in the
        implementation are requiring different number of memory objects.
        The upper multiplicity of this role has been increased to * due
        to resolving an atpVariation stereotype. The previous value was
        -1.
    :ivar constant_value_mapping_refs: Reference to the
        ConstanSpecificationMapping to be applied for the particular
        InternalBehavior
    :ivar data_type_mapping_refs: Reference to the DataTypeMapping to be
        applied for the particular InternalBehavior
    :ivar exclusive_areas: This specifies an ExclusiveArea for this
        InternalBehavior. The exclusiveArea is local to the component
        resp. module. The aggregation of ExclusiveAreas is subject to
        variability. Note: the number of ExclusiveAreas might vary due
        to the conditional existence of RunnableEntities or
        BswModuleEntities. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar exclusive_area_nesting_orders: This represents the set of
        ExclusiveAreaNestingOrder owned by the InternalBehavior. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar static_memorys: Describes a read and writeable static memory
        object representing measurerment variables implemented by this
        software component. The term "static" is used in the meaning of
        "non-temporary" and does not necessarily specify a linker
        encapsulation. This kind of memory is only supported if
        supportsMultipleInstantiation is FALSE. The shortName of the
        VariableDataPrototype has to be equal with the ''C' identifier
        of the described variable. The aggregation of staticMemory is
        subject to variability with the purpose to support variability
        in the software component's implementations. Typically different
        algorithms in the implementation are requiring different number
        of memory objects. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar ar_typed_per_instance_memorys: Defines an AUTOSAR typed
        memory-block that needs to be available for each instance of the
        Basic Software Module. The aggregation of
        arTypedPerInstanceMemory is subject to variability with the
        purpose to support variability in the Basic Software Module's
        implementations. Typically different algorithms in the
        implementation are requiring different number of memory objects.
        The upper multiplicity of this role has been increased to * due
        to resolving an atpVariation stereotype. The previous value was
        -1.
    :ivar bsw_per_instance_memory_policys: Policy for a
        arTypedPerInstanceMemory The policy selects the options of the
        Schedule Manager API generation. The upper multiplicity of this
        role has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
    :ivar client_policys: Policy for a requiredClientServerEntry. The
        policy selects the options of the Schedule Manager API
        generation. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar exclusive_area_policys: Policy for an  ExclusiveArea in this
        BswInternalBehavior. The policy selects the options of the
        Schedule Manager API generation. The upper multiplicity of this
        role has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
    :ivar included_data_type_sets: The includedDataTypeSet is used by a
        basic software module for its implementation.
    :ivar internal_triggering_point_policys: Policy for an
        internalTriggeringPoint in this BswInternalBehavior.. The policy
        selects the options of the Schedule Manager API generation. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar parameter_policys: Policy for a  perInstanceParameter in this
        BswInternalBehavior. The policy selects the options of the
        Schedule Manager API generation. The upper multiplicity of this
        role has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
    :ivar released_trigger_policys: Policy for a  releasedTrigger. The
        policy selects the options of the Schedule Manager API
        generation. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar send_policys: Policy for a providedData. The policy selects
        the options of the Schedule Manager API generation. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar variation_point_proxys: Proxy of a variation points in the
        C/C++ implementation.
    :ivar internal_triggering_points: An internal triggering point. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar entitys: A code entity for which the behavior is described The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar events: An event required by this module behavior. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar trigger_direct_implementations: Specifies a trigger to be
        directly implemented via OS calls. The upper multiplicity of
        this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was -1.
    :ivar mode_sender_policys: Implementation policy for providing a
        mode group. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar mode_receiver_policys: Implementation policy for the reception
        of mode switches. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar service_dependencys: Defines the requirements on AUTOSAR
        Services for a particular item. The aggregation is subject to
        variability with the purpose to support the conditional
        existence of ServiceNeeds. The aggregation is splitable in order
        to support that ServiceNeeds might be provided in later
        development steps. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar per_instance_parameters: Describes a read only memory object
        containing characteristic value(s)  needed by this
        BswInternalBehavior. The role name perInstanceParameter is
        chosen in analogy to the similar role in the context of
        SwcInternalBehavior. In contrast to constantMemory, this object
        is not allocated locally by the module's code, but by the BSW
        Scheduler and it is accessed from the BSW module via the BSW
        Scheduler API. The main use case is the support of software
        emulation of calibration data. The aggregation is subject to
        variability with the purpose to support implementation variants.
        The upper multiplicity of this role has been increased to * due
        to resolving an atpVariation stereotype. The previous value was
        -1.
    :ivar scheduler_name_prefixs: Optional definition of one or more
        prefixes to be used for the BswScheduler. The upper multiplicity
        of this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was -1.
    :ivar reception_policys: Data reception policy for inter-partition
        and/or inter-core communication. The upper multiplicity of this
        role has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
    :ivar distinguished_partitions: Indicates an abstract partition
        context in which the enclosing BswModuleEntity can be executed.
        The upper multiplicity of this role has been increased to * due
        to resolving an atpVariation stereotype. The previous value was
        -1.
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
        name = "BSW-INTERNAL-BEHAVIOR"

    short_name: Identifier = field(
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: None | BswInternalBehavior.ShortNameFragments = (
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
    annotations: None | BswInternalBehavior.Annotations = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    constant_memorys: None | BswInternalBehavior.ConstantMemorys = field(
        default=None,
        metadata={
            "name": "CONSTANT-MEMORYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    constant_value_mapping_refs: (
        None | BswInternalBehavior.ConstantValueMappingRefs
    ) = field(
        default=None,
        metadata={
            "name": "CONSTANT-VALUE-MAPPING-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_type_mapping_refs: None | BswInternalBehavior.DataTypeMappingRefs = (
        field(
            default=None,
            metadata={
                "name": "DATA-TYPE-MAPPING-REFS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    exclusive_areas: None | BswInternalBehavior.ExclusiveAreas = field(
        default=None,
        metadata={
            "name": "EXCLUSIVE-AREAS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    exclusive_area_nesting_orders: (
        None | BswInternalBehavior.ExclusiveAreaNestingOrders
    ) = field(
        default=None,
        metadata={
            "name": "EXCLUSIVE-AREA-NESTING-ORDERS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    static_memorys: None | BswInternalBehavior.StaticMemorys = field(
        default=None,
        metadata={
            "name": "STATIC-MEMORYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ar_typed_per_instance_memorys: (
        None | BswInternalBehavior.ArTypedPerInstanceMemorys
    ) = field(
        default=None,
        metadata={
            "name": "AR-TYPED-PER-INSTANCE-MEMORYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    bsw_per_instance_memory_policys: (
        None | BswInternalBehavior.BswPerInstanceMemoryPolicys
    ) = field(
        default=None,
        metadata={
            "name": "BSW-PER-INSTANCE-MEMORY-POLICYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    client_policys: None | BswInternalBehavior.ClientPolicys = field(
        default=None,
        metadata={
            "name": "CLIENT-POLICYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    exclusive_area_policys: None | BswInternalBehavior.ExclusiveAreaPolicys = (
        field(
            default=None,
            metadata={
                "name": "EXCLUSIVE-AREA-POLICYS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    included_data_type_sets: (
        None | BswInternalBehavior.IncludedDataTypeSets
    ) = field(
        default=None,
        metadata={
            "name": "INCLUDED-DATA-TYPE-SETS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    internal_triggering_point_policys: (
        None | BswInternalBehavior.InternalTriggeringPointPolicys
    ) = field(
        default=None,
        metadata={
            "name": "INTERNAL-TRIGGERING-POINT-POLICYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    parameter_policys: None | BswInternalBehavior.ParameterPolicys = field(
        default=None,
        metadata={
            "name": "PARAMETER-POLICYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    released_trigger_policys: (
        None | BswInternalBehavior.ReleasedTriggerPolicys
    ) = field(
        default=None,
        metadata={
            "name": "RELEASED-TRIGGER-POLICYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    send_policys: None | BswInternalBehavior.SendPolicys = field(
        default=None,
        metadata={
            "name": "SEND-POLICYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point_proxys: None | BswInternalBehavior.VariationPointProxys = (
        field(
            default=None,
            metadata={
                "name": "VARIATION-POINT-PROXYS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    internal_triggering_points: (
        None | BswInternalBehavior.InternalTriggeringPoints
    ) = field(
        default=None,
        metadata={
            "name": "INTERNAL-TRIGGERING-POINTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    entitys: None | BswInternalBehavior.Entitys = field(
        default=None,
        metadata={
            "name": "ENTITYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    events: None | BswInternalBehavior.Events = field(
        default=None,
        metadata={
            "name": "EVENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    trigger_direct_implementations: (
        None | BswInternalBehavior.TriggerDirectImplementations
    ) = field(
        default=None,
        metadata={
            "name": "TRIGGER-DIRECT-IMPLEMENTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mode_sender_policys: None | BswInternalBehavior.ModeSenderPolicys = field(
        default=None,
        metadata={
            "name": "MODE-SENDER-POLICYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mode_receiver_policys: None | BswInternalBehavior.ModeReceiverPolicys = (
        field(
            default=None,
            metadata={
                "name": "MODE-RECEIVER-POLICYS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    service_dependencys: None | BswInternalBehavior.ServiceDependencys = field(
        default=None,
        metadata={
            "name": "SERVICE-DEPENDENCYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    per_instance_parameters: (
        None | BswInternalBehavior.PerInstanceParameters
    ) = field(
        default=None,
        metadata={
            "name": "PER-INSTANCE-PARAMETERS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    scheduler_name_prefixs: None | BswInternalBehavior.SchedulerNamePrefixs = (
        field(
            default=None,
            metadata={
                "name": "SCHEDULER-NAME-PREFIXS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    reception_policys: None | BswInternalBehavior.ReceptionPolicys = field(
        default=None,
        metadata={
            "name": "RECEPTION-POLICYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    distinguished_partitions: (
        None | BswInternalBehavior.DistinguishedPartitions
    ) = field(
        default=None,
        metadata={
            "name": "DISTINGUISHED-PARTITIONS",
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
    class ConstantMemorys:
        parameter_data_prototype: list[ParameterDataPrototype] = field(
            default_factory=list,
            metadata={
                "name": "PARAMETER-DATA-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class ConstantValueMappingRefs:
        constant_value_mapping_ref: list[
            BswInternalBehavior.ConstantValueMappingRefs.ConstantValueMappingRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "CONSTANT-VALUE-MAPPING-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass(kw_only=True)
        class ConstantValueMappingRef(Ref):
            dest: ConstantSpecificationMappingSetSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass(kw_only=True)
    class DataTypeMappingRefs:
        data_type_mapping_ref: list[
            BswInternalBehavior.DataTypeMappingRefs.DataTypeMappingRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "DATA-TYPE-MAPPING-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass(kw_only=True)
        class DataTypeMappingRef(Ref):
            dest: DataTypeMappingSetSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass(kw_only=True)
    class ExclusiveAreas:
        exclusive_area: list[ExclusiveArea] = field(
            default_factory=list,
            metadata={
                "name": "EXCLUSIVE-AREA",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class ExclusiveAreaNestingOrders:
        exclusive_area_nesting_order: list[ExclusiveAreaNestingOrder] = field(
            default_factory=list,
            metadata={
                "name": "EXCLUSIVE-AREA-NESTING-ORDER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class StaticMemorys:
        variable_data_prototype: list[VariableDataPrototype] = field(
            default_factory=list,
            metadata={
                "name": "VARIABLE-DATA-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class ArTypedPerInstanceMemorys:
        variable_data_prototype: list[VariableDataPrototype] = field(
            default_factory=list,
            metadata={
                "name": "VARIABLE-DATA-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class BswPerInstanceMemoryPolicys:
        bsw_per_instance_memory_policy: list[BswPerInstanceMemoryPolicy] = (
            field(
                default_factory=list,
                metadata={
                    "name": "BSW-PER-INSTANCE-MEMORY-POLICY",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )

    @dataclass(kw_only=True)
    class ClientPolicys:
        bsw_client_policy: list[BswClientPolicy] = field(
            default_factory=list,
            metadata={
                "name": "BSW-CLIENT-POLICY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class ExclusiveAreaPolicys:
        bsw_exclusive_area_policy: list[BswExclusiveAreaPolicy] = field(
            default_factory=list,
            metadata={
                "name": "BSW-EXCLUSIVE-AREA-POLICY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class IncludedDataTypeSets:
        included_data_type_set: list[IncludedDataTypeSet] = field(
            default_factory=list,
            metadata={
                "name": "INCLUDED-DATA-TYPE-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class InternalTriggeringPointPolicys:
        bsw_internal_triggering_point_policy: list[
            BswInternalTriggeringPointPolicy
        ] = field(
            default_factory=list,
            metadata={
                "name": "BSW-INTERNAL-TRIGGERING-POINT-POLICY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class ParameterPolicys:
        bsw_parameter_policy: list[BswParameterPolicy] = field(
            default_factory=list,
            metadata={
                "name": "BSW-PARAMETER-POLICY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class ReleasedTriggerPolicys:
        bsw_released_trigger_policy: list[BswReleasedTriggerPolicy] = field(
            default_factory=list,
            metadata={
                "name": "BSW-RELEASED-TRIGGER-POLICY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class SendPolicys:
        bsw_data_send_policy: list[BswDataSendPolicy] = field(
            default_factory=list,
            metadata={
                "name": "BSW-DATA-SEND-POLICY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class VariationPointProxys:
        variation_point_proxy: list[VariationPointProxy] = field(
            default_factory=list,
            metadata={
                "name": "VARIATION-POINT-PROXY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class InternalTriggeringPoints:
        bsw_internal_triggering_point: list[BswInternalTriggeringPoint] = (
            field(
                default_factory=list,
                metadata={
                    "name": "BSW-INTERNAL-TRIGGERING-POINT",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )

    @dataclass(kw_only=True)
    class Entitys:
        bsw_called_entity: list[BswCalledEntity] = field(
            default_factory=list,
            metadata={
                "name": "BSW-CALLED-ENTITY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bsw_interrupt_entity: list[BswInterruptEntity] = field(
            default_factory=list,
            metadata={
                "name": "BSW-INTERRUPT-ENTITY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bsw_schedulable_entity: list[BswSchedulableEntity] = field(
            default_factory=list,
            metadata={
                "name": "BSW-SCHEDULABLE-ENTITY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class Events:
        bsw_asynchronous_server_call_returns_event: list[
            BswAsynchronousServerCallReturnsEvent
        ] = field(
            default_factory=list,
            metadata={
                "name": "BSW-ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bsw_background_event: list[BswBackgroundEvent] = field(
            default_factory=list,
            metadata={
                "name": "BSW-BACKGROUND-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bsw_data_received_event: list[BswDataReceivedEvent] = field(
            default_factory=list,
            metadata={
                "name": "BSW-DATA-RECEIVED-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bsw_external_trigger_occurred_event: list[
            BswExternalTriggerOccurredEvent
        ] = field(
            default_factory=list,
            metadata={
                "name": "BSW-EXTERNAL-TRIGGER-OCCURRED-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bsw_internal_trigger_occurred_event: list[
            BswInternalTriggerOccurredEvent
        ] = field(
            default_factory=list,
            metadata={
                "name": "BSW-INTERNAL-TRIGGER-OCCURRED-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bsw_mode_manager_error_event: list[BswModeManagerErrorEvent] = field(
            default_factory=list,
            metadata={
                "name": "BSW-MODE-MANAGER-ERROR-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bsw_mode_switch_event: list[BswModeSwitchEvent] = field(
            default_factory=list,
            metadata={
                "name": "BSW-MODE-SWITCH-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bsw_mode_switched_ack_event: list[BswModeSwitchedAckEvent] = field(
            default_factory=list,
            metadata={
                "name": "BSW-MODE-SWITCHED-ACK-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bsw_operation_invoked_event: list[BswOperationInvokedEvent] = field(
            default_factory=list,
            metadata={
                "name": "BSW-OPERATION-INVOKED-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bsw_os_task_execution_event: list[BswOsTaskExecutionEvent] = field(
            default_factory=list,
            metadata={
                "name": "BSW-OS-TASK-EXECUTION-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        bsw_timing_event: list[BswTimingEvent] = field(
            default_factory=list,
            metadata={
                "name": "BSW-TIMING-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class TriggerDirectImplementations:
        bsw_trigger_direct_implementation: list[
            BswTriggerDirectImplementation
        ] = field(
            default_factory=list,
            metadata={
                "name": "BSW-TRIGGER-DIRECT-IMPLEMENTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class ModeSenderPolicys:
        bsw_mode_sender_policy: list[BswModeSenderPolicy] = field(
            default_factory=list,
            metadata={
                "name": "BSW-MODE-SENDER-POLICY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class ModeReceiverPolicys:
        bsw_mode_receiver_policy: list[BswModeReceiverPolicy] = field(
            default_factory=list,
            metadata={
                "name": "BSW-MODE-RECEIVER-POLICY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class ServiceDependencys:
        bsw_service_dependency: list[BswServiceDependency] = field(
            default_factory=list,
            metadata={
                "name": "BSW-SERVICE-DEPENDENCY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class PerInstanceParameters:
        parameter_data_prototype: list[ParameterDataPrototype] = field(
            default_factory=list,
            metadata={
                "name": "PARAMETER-DATA-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class SchedulerNamePrefixs:
        bsw_scheduler_name_prefix: list[BswSchedulerNamePrefix] = field(
            default_factory=list,
            metadata={
                "name": "BSW-SCHEDULER-NAME-PREFIX",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class ReceptionPolicys:
        bsw_queued_data_reception_policy: list[
            BswQueuedDataReceptionPolicy
        ] = field(
            default_factory=list,
            metadata={
                "name": "BSW-QUEUED-DATA-RECEPTION-POLICY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class DistinguishedPartitions:
        bsw_distinguished_partition: list[BswDistinguishedPartition] = field(
            default_factory=list,
            metadata={
                "name": "BSW-DISTINGUISHED-PARTITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
