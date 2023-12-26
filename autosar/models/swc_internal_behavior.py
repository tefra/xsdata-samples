from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .asynchronous_server_call_returns_event import (
    AsynchronousServerCallReturnsEvent,
)
from .background_event import BackgroundEvent
from .boolean import Boolean
from .category_string import CategoryString
from .constant_specification_mapping_set_subtypes_enum import (
    ConstantSpecificationMappingSetSubtypesEnum,
)
from .data_receive_error_event import DataReceiveErrorEvent
from .data_received_event import DataReceivedEvent
from .data_send_completed_event import DataSendCompletedEvent
from .data_type_mapping_set_subtypes_enum import DataTypeMappingSetSubtypesEnum
from .data_write_completed_event import DataWriteCompletedEvent
from .exclusive_area import ExclusiveArea
from .exclusive_area_nesting_order import ExclusiveAreaNestingOrder
from .external_trigger_occurred_event import ExternalTriggerOccurredEvent
from .handle_termination_and_restart_enum import (
    HandleTerminationAndRestartEnum,
)
from .identifier import Identifier
from .included_data_type_set import IncludedDataTypeSet
from .included_mode_declaration_group_set import (
    IncludedModeDeclarationGroupSet,
)
from .init_event import InitEvent
from .instantiation_data_def_props import InstantiationDataDefProps
from .internal_trigger_occurred_event import InternalTriggerOccurredEvent
from .mode_switched_ack_event import ModeSwitchedAckEvent
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .operation_invoked_event import OperationInvokedEvent
from .os_task_execution_event import OsTaskExecutionEvent
from .parameter_data_prototype import ParameterDataPrototype
from .per_instance_memory import PerInstanceMemory
from .port_api_option import PortApiOption
from .ref import Ref
from .runnable_entity import RunnableEntity
from .short_name_fragment import ShortNameFragment
from .swc_exclusive_area_policy import SwcExclusiveAreaPolicy
from .swc_mode_manager_error_event import SwcModeManagerErrorEvent
from .swc_mode_switch_event import SwcModeSwitchEvent
from .swc_service_dependency import SwcServiceDependency
from .timing_event import TimingEvent
from .transformer_hard_error_event import TransformerHardErrorEvent
from .variable_data_prototype import VariableDataPrototype
from .variation_point_proxy import VariationPointProxy

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwcInternalBehavior:
    """
    The SwcInternalBehavior of an AtomicSwComponentType describes the relevant
    aspects of the software-component with respect to the RTE, i.e. the
    RunnableEntities and the RTEEvents they respond to.

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
        SW-component. This is typically only useful if
        supportsMultipleInstantiation is set to "true" or if the
        component defines NVRAM access via permanent blocks. The
        aggregation of arTypedPerInstanceMemory is subject to
        variability with the purpose to support variability in the
        software component's implementations. Typically different
        algorithms in the implementation are requiring different number
        of memory objects. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar events: This is a RTEEvent specified for the particular
        SwcInternalBehavior. The aggregation of RTEEvent is subject to
        variability with the purpose to support the conditional
        existence of RTE events. Note: the number of RTE events might
        vary due to the conditional existence of PortPrototypes using
        DataReceivedEvents or due to different scheduling needs of
        algorithms. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar exclusive_area_policys: Options how to generate the
        ExclusiveArea related APIs. When no SwcExclusiveAreaPolicy is
        specified for an ExclusiveArea the default values apply. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar explicit_inter_runnable_variables: Implement state message
        semantics for establishing communication among runnables of the
        same component. The aggregation of explicitInterRunnableVariable
        is subject to variability with the purpose to support
        variability in the software components implementations.
        Typically different algorithms in the implementation are
        requiring different number of memory objects. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar handle_termination_and_restart: This attribute controls the
        behavior with respect to stopping and restarting. The
        corresponding AtomicSwComponentType may either not support stop
        and restart, or support only stop, or support both stop and
        restart.
    :ivar implicit_inter_runnable_variables: Implement state message
        semantics for establishing communication among runnables of the
        same component. The aggregation of implicitInterRunnableVariable
        is subject to variability with the purpose to support
        variability in the software components implementations.
        Typically different algorithms in the implementation are
        requiring different number of memory objects. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar included_data_type_sets: The includedDataTypeSet is used by a
        software component for its implementation.
    :ivar included_mode_declaration_group_sets: This aggregation
        represents the included ModeDeclarationGroups
    :ivar instantiation_data_def_propss: The purpose of this is that
        within the context  of a given SwComponentType some data def
        properties of individual instantiations can be  modified. The
        aggregation of InstantiationDataDefProps is subject to
        variability with the purpose to support the conditional
        existence of PortPrototypes and component local memories like
        "perInstanceParameter" or "arTypedPerInstanceMemory". The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar per_instance_memorys: Defines a per-instance memory object
        needed by this software component. The aggregation of
        PerInstanceMemory is subject to variability with the purpose to
        support variability in the software components implementations.
        Typically different algorithms in the implementation are
        requiring different number of memory objects. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar per_instance_parameters: Defines parameter(s) or
        characteristic value(s) that needs to be available for each
        instance of the software-component. This is typically only
        useful if supportsMultipleInstantiation is set to "true". The
        aggregation of perInstanceParameter is subject to variability
        with the purpose to support variability in the software
        components implementations. Typically different algorithms in
        the implementation are requiring different number of memory
        objects. The upper multiplicity of this role has been increased
        to * due to resolving an atpVariation stereotype. The previous
        value was -1.
    :ivar port_api_options: Options for generating the signature of
        port-related calls from a runnable to the RTE and vice versa.
        The aggregation of PortPrototypes is subject to variability with
        the purpose to support the conditional existence of ports. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar runnables: This is a RunnableEntity specified for the
        particular SwcInternalBehavior. The aggregation of
        RunnableEntity is subject to variability with the purpose to
        support the conditional existence of RunnableEntities. Note: the
        number of RunnableEntities might vary due to the conditional
        existence of PortPrototypes using DataReceivedEvents or due to
        different scheduling needs of algorithms. The upper multiplicity
        of this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was -1.
    :ivar service_dependencys: Defines the requirements on AUTOSAR
        Services for a particular item. The aggregation of
        SwcServiceDependency is subject to variability with the purpose
        to support the conditional existence of ports as well as the
        conditional existence of ServiceNeeds. The SwcServiceDependency
        owned by an SwcInternalBehavior can be located in a different
        physical file in order to support that SwcServiceDependency
        might be provided in later development steps or even by
        different expert domain (e.g OBD expert for Obd related  Service
        Needs) tools. Therefore the aggregation is
        &lt;&lt;atpSplitable&gt;&gt;. The upper multiplicity of this
        role has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
    :ivar shared_parameters: Defines parameter(s) or characteristic
        value(s) shared between SwComponentPrototypes of the same
        SwComponentType The aggregation of sharedParameter is subject to
        variability with the purpose to support variability in the
        software components implementations. Typically different
        algorithms in the implementation are requiring different number
        of memory objects. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar supports_multiple_instantiation: Indicate whether the
        corresponding software-component can be multiply instantiated on
        one ECU. In this case the attribute will result in an
        appropriate component API on programming language level (with or
        without instance handle).
    :ivar variation_point_proxys: Proxy of a variation points in the
        C/C++ implementation.
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
        name = "SWC-INTERNAL-BEHAVIOR"

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
        "SwcInternalBehavior.ShortNameFragments"
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
    annotations: Optional["SwcInternalBehavior.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    constant_memorys: Optional["SwcInternalBehavior.ConstantMemorys"] = field(
        default=None,
        metadata={
            "name": "CONSTANT-MEMORYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    constant_value_mapping_refs: Optional[
        "SwcInternalBehavior.ConstantValueMappingRefs"
    ] = field(
        default=None,
        metadata={
            "name": "CONSTANT-VALUE-MAPPING-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_type_mapping_refs: Optional[
        "SwcInternalBehavior.DataTypeMappingRefs"
    ] = field(
        default=None,
        metadata={
            "name": "DATA-TYPE-MAPPING-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    exclusive_areas: Optional["SwcInternalBehavior.ExclusiveAreas"] = field(
        default=None,
        metadata={
            "name": "EXCLUSIVE-AREAS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    exclusive_area_nesting_orders: Optional[
        "SwcInternalBehavior.ExclusiveAreaNestingOrders"
    ] = field(
        default=None,
        metadata={
            "name": "EXCLUSIVE-AREA-NESTING-ORDERS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    static_memorys: Optional["SwcInternalBehavior.StaticMemorys"] = field(
        default=None,
        metadata={
            "name": "STATIC-MEMORYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ar_typed_per_instance_memorys: Optional[
        "SwcInternalBehavior.ArTypedPerInstanceMemorys"
    ] = field(
        default=None,
        metadata={
            "name": "AR-TYPED-PER-INSTANCE-MEMORYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    events: Optional["SwcInternalBehavior.Events"] = field(
        default=None,
        metadata={
            "name": "EVENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    exclusive_area_policys: Optional[
        "SwcInternalBehavior.ExclusiveAreaPolicys"
    ] = field(
        default=None,
        metadata={
            "name": "EXCLUSIVE-AREA-POLICYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    explicit_inter_runnable_variables: Optional[
        "SwcInternalBehavior.ExplicitInterRunnableVariables"
    ] = field(
        default=None,
        metadata={
            "name": "EXPLICIT-INTER-RUNNABLE-VARIABLES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    handle_termination_and_restart: Optional[
        HandleTerminationAndRestartEnum
    ] = field(
        default=None,
        metadata={
            "name": "HANDLE-TERMINATION-AND-RESTART",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    implicit_inter_runnable_variables: Optional[
        "SwcInternalBehavior.ImplicitInterRunnableVariables"
    ] = field(
        default=None,
        metadata={
            "name": "IMPLICIT-INTER-RUNNABLE-VARIABLES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    included_data_type_sets: Optional[
        "SwcInternalBehavior.IncludedDataTypeSets"
    ] = field(
        default=None,
        metadata={
            "name": "INCLUDED-DATA-TYPE-SETS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    included_mode_declaration_group_sets: Optional[
        "SwcInternalBehavior.IncludedModeDeclarationGroupSets"
    ] = field(
        default=None,
        metadata={
            "name": "INCLUDED-MODE-DECLARATION-GROUP-SETS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    instantiation_data_def_propss: Optional[
        "SwcInternalBehavior.InstantiationDataDefPropss"
    ] = field(
        default=None,
        metadata={
            "name": "INSTANTIATION-DATA-DEF-PROPSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    per_instance_memorys: Optional[
        "SwcInternalBehavior.PerInstanceMemorys"
    ] = field(
        default=None,
        metadata={
            "name": "PER-INSTANCE-MEMORYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    per_instance_parameters: Optional[
        "SwcInternalBehavior.PerInstanceParameters"
    ] = field(
        default=None,
        metadata={
            "name": "PER-INSTANCE-PARAMETERS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    port_api_options: Optional["SwcInternalBehavior.PortApiOptions"] = field(
        default=None,
        metadata={
            "name": "PORT-API-OPTIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    runnables: Optional["SwcInternalBehavior.Runnables"] = field(
        default=None,
        metadata={
            "name": "RUNNABLES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    service_dependencys: Optional[
        "SwcInternalBehavior.ServiceDependencys"
    ] = field(
        default=None,
        metadata={
            "name": "SERVICE-DEPENDENCYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    shared_parameters: Optional[
        "SwcInternalBehavior.SharedParameters"
    ] = field(
        default=None,
        metadata={
            "name": "SHARED-PARAMETERS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    supports_multiple_instantiation: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "SUPPORTS-MULTIPLE-INSTANTIATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point_proxys: Optional[
        "SwcInternalBehavior.VariationPointProxys"
    ] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT-PROXYS",
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
    class ConstantMemorys:
        parameter_data_prototype: List[ParameterDataPrototype] = field(
            default_factory=list,
            metadata={
                "name": "PARAMETER-DATA-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ConstantValueMappingRefs:
        constant_value_mapping_ref: List[
            "SwcInternalBehavior.ConstantValueMappingRefs.ConstantValueMappingRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "CONSTANT-VALUE-MAPPING-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ConstantValueMappingRef(Ref):
            dest: Optional[
                ConstantSpecificationMappingSetSubtypesEnum
            ] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class DataTypeMappingRefs:
        data_type_mapping_ref: List[
            "SwcInternalBehavior.DataTypeMappingRefs.DataTypeMappingRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "DATA-TYPE-MAPPING-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class DataTypeMappingRef(Ref):
            dest: Optional[DataTypeMappingSetSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class ExclusiveAreas:
        exclusive_area: List[ExclusiveArea] = field(
            default_factory=list,
            metadata={
                "name": "EXCLUSIVE-AREA",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ExclusiveAreaNestingOrders:
        exclusive_area_nesting_order: List[ExclusiveAreaNestingOrder] = field(
            default_factory=list,
            metadata={
                "name": "EXCLUSIVE-AREA-NESTING-ORDER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class StaticMemorys:
        variable_data_prototype: List[VariableDataPrototype] = field(
            default_factory=list,
            metadata={
                "name": "VARIABLE-DATA-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ArTypedPerInstanceMemorys:
        variable_data_prototype: List[VariableDataPrototype] = field(
            default_factory=list,
            metadata={
                "name": "VARIABLE-DATA-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Events:
        asynchronous_server_call_returns_event: List[
            AsynchronousServerCallReturnsEvent
        ] = field(
            default_factory=list,
            metadata={
                "name": "ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        background_event: List[BackgroundEvent] = field(
            default_factory=list,
            metadata={
                "name": "BACKGROUND-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        data_receive_error_event: List[DataReceiveErrorEvent] = field(
            default_factory=list,
            metadata={
                "name": "DATA-RECEIVE-ERROR-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        data_received_event: List[DataReceivedEvent] = field(
            default_factory=list,
            metadata={
                "name": "DATA-RECEIVED-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        data_send_completed_event: List[DataSendCompletedEvent] = field(
            default_factory=list,
            metadata={
                "name": "DATA-SEND-COMPLETED-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        data_write_completed_event: List[DataWriteCompletedEvent] = field(
            default_factory=list,
            metadata={
                "name": "DATA-WRITE-COMPLETED-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        external_trigger_occurred_event: List[
            ExternalTriggerOccurredEvent
        ] = field(
            default_factory=list,
            metadata={
                "name": "EXTERNAL-TRIGGER-OCCURRED-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        init_event: List[InitEvent] = field(
            default_factory=list,
            metadata={
                "name": "INIT-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        internal_trigger_occurred_event: List[
            InternalTriggerOccurredEvent
        ] = field(
            default_factory=list,
            metadata={
                "name": "INTERNAL-TRIGGER-OCCURRED-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        mode_switched_ack_event: List[ModeSwitchedAckEvent] = field(
            default_factory=list,
            metadata={
                "name": "MODE-SWITCHED-ACK-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        operation_invoked_event: List[OperationInvokedEvent] = field(
            default_factory=list,
            metadata={
                "name": "OPERATION-INVOKED-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        os_task_execution_event: List[OsTaskExecutionEvent] = field(
            default_factory=list,
            metadata={
                "name": "OS-TASK-EXECUTION-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        swc_mode_manager_error_event: List[SwcModeManagerErrorEvent] = field(
            default_factory=list,
            metadata={
                "name": "SWC-MODE-MANAGER-ERROR-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        swc_mode_switch_event: List[SwcModeSwitchEvent] = field(
            default_factory=list,
            metadata={
                "name": "SWC-MODE-SWITCH-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        timing_event: List[TimingEvent] = field(
            default_factory=list,
            metadata={
                "name": "TIMING-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        transformer_hard_error_event: List[TransformerHardErrorEvent] = field(
            default_factory=list,
            metadata={
                "name": "TRANSFORMER-HARD-ERROR-EVENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ExclusiveAreaPolicys:
        swc_exclusive_area_policy: List[SwcExclusiveAreaPolicy] = field(
            default_factory=list,
            metadata={
                "name": "SWC-EXCLUSIVE-AREA-POLICY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ExplicitInterRunnableVariables:
        variable_data_prototype: List[VariableDataPrototype] = field(
            default_factory=list,
            metadata={
                "name": "VARIABLE-DATA-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ImplicitInterRunnableVariables:
        variable_data_prototype: List[VariableDataPrototype] = field(
            default_factory=list,
            metadata={
                "name": "VARIABLE-DATA-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class IncludedDataTypeSets:
        included_data_type_set: List[IncludedDataTypeSet] = field(
            default_factory=list,
            metadata={
                "name": "INCLUDED-DATA-TYPE-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class IncludedModeDeclarationGroupSets:
        included_mode_declaration_group_set: List[
            IncludedModeDeclarationGroupSet
        ] = field(
            default_factory=list,
            metadata={
                "name": "INCLUDED-MODE-DECLARATION-GROUP-SET",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class InstantiationDataDefPropss:
        instantiation_data_def_props: List[InstantiationDataDefProps] = field(
            default_factory=list,
            metadata={
                "name": "INSTANTIATION-DATA-DEF-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class PerInstanceMemorys:
        per_instance_memory: List[PerInstanceMemory] = field(
            default_factory=list,
            metadata={
                "name": "PER-INSTANCE-MEMORY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class PerInstanceParameters:
        parameter_data_prototype: List[ParameterDataPrototype] = field(
            default_factory=list,
            metadata={
                "name": "PARAMETER-DATA-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class PortApiOptions:
        port_api_option: List[PortApiOption] = field(
            default_factory=list,
            metadata={
                "name": "PORT-API-OPTION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Runnables:
        runnable_entity: List[RunnableEntity] = field(
            default_factory=list,
            metadata={
                "name": "RUNNABLE-ENTITY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ServiceDependencys:
        swc_service_dependency: List[SwcServiceDependency] = field(
            default_factory=list,
            metadata={
                "name": "SWC-SERVICE-DEPENDENCY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class SharedParameters:
        parameter_data_prototype: List[ParameterDataPrototype] = field(
            default_factory=list,
            metadata={
                "name": "PARAMETER-DATA-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class VariationPointProxys:
        variation_point_proxy: List[VariationPointProxy] = field(
            default_factory=list,
            metadata={
                "name": "VARIATION-POINT-PROXY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
