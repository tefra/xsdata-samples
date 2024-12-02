from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .asynchronous_server_call_point import AsynchronousServerCallPoint
from .asynchronous_server_call_result_point import (
    AsynchronousServerCallResultPoint,
)
from .boolean import Boolean
from .c_identifier import CIdentifier
from .category_string import CategoryString
from .exclusive_area_nesting_order_subtypes_enum import (
    ExclusiveAreaNestingOrderSubtypesEnum,
)
from .exclusive_area_subtypes_enum import ExclusiveAreaSubtypesEnum
from .executable_entity_activation_reason import (
    ExecutableEntityActivationReason,
)
from .external_triggering_point import ExternalTriggeringPoint
from .identifier import Identifier
from .internal_triggering_point import InternalTriggeringPoint
from .mode_access_point import ModeAccessPoint
from .mode_switch_point import ModeSwitchPoint
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .parameter_access import ParameterAccess
from .reentrancy_level_enum import ReentrancyLevelEnum
from .ref import Ref
from .runnable_entity_argument import RunnableEntityArgument
from .short_name_fragment import ShortNameFragment
from .sw_addr_method_subtypes_enum import SwAddrMethodSubtypesEnum
from .synchronous_server_call_point import SynchronousServerCallPoint
from .time_value import TimeValue
from .variable_access import VariableAccess
from .wait_point import WaitPoint

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RunnableEntity:
    """A RunnableEntity represents the smallest code-fragment that is provided by
    an AtomicSwComponentType and are executed under control of the RTE.

    RunnableEntities are for instance set up to respond to data
    reception or operation invocation on a server.

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
    :ivar activation_reasons: If the ExecutableEntity provides at least
        one activationReason element the RTE resp. BSW Scheduler shall
        provide means to read the activation vector of this executable
        entity execution. If no activationReason element is provided the
        feature of being able to determine the activating RTEEvent is
        disabled for this ExecutableEntity.
    :ivar can_enter_exclusive_area_refs: This means that the executable
        entity can enter/leave the referenced exclusive area through
        explicit API calls.
    :ivar exclusive_area_nesting_order_refs: This represents the set of
        ExclusiveAreaNestingOrders recognized by this ExecutableEntity.
    :ivar minimum_start_interval: Specifies the time in seconds by which
        two consecutive starts of an ExecutableEntity are guaranteed to
        be separated.
    :ivar reentrancy_level: The reentrancy level of this
        ExecutableEntity. See the documentation of the enumeration type
        ReentrancyLevelEnum for details. Please note that nonReentrant
        interfaces can have also reentrant or multicoreReentrant
        implementations, and reentrant interfaces can also have
        multicoreReentrant implementations.
    :ivar runs_inside_exclusive_area_refs: The executable entity runs
        completely inside the referenced exclusive area.
    :ivar sw_addr_method_ref: Addressing method related to this code
        entity. Via an association to the same SwAddrMethod, it can be
        specified that several code entities (even of different modules
        or components)  shall be located in the same memory without
        already specifying the memory section itself.
    :ivar arguments: This represents the formal definition of a an
        argument to a RunnableEntity.
    :ivar asynchronous_server_call_result_points: The server call result
        point admits a runnable to fetch the result of an asynchronous
        server call. The aggregation of
        AsynchronousServerCallResultPoint is subject to variability with
        the purpose to support the conditional existence of client
        server PortPrototypes and the variant existence of server call
        result points in the implementation. The upper multiplicity of
        this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was -1.
    :ivar can_be_invoked_concurrently: If the value of this attribute is
        set to "true" the enclosing RunnableEntity can be invoked
        concurrently (even for one instance of the corresponding
        AtomicSwComponentType). This implies that it is the
        responsibility of the implementation of the RunnableEntity to
        take care of this form of concurrency. Note that the default
        value of this attribute is set to "false".
    :ivar data_read_accesss: RunnableEntity has implicit read access to
        dataElement of a sender-receiver PortPrototype or nv data of a
        nv data PortPrototype. The aggregation of dataReadAccess is
        subject to variability with the purpose to support the
        conditional existence of sender receiver ports or the variant
        existence of dataReadAccess in the implementation. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar data_receive_point_by_arguments: RunnableEntity has explicit
        read access to dataElement of a sender-receiver PortPrototype or
        nv data of a nv data PortPrototype. The result is passed back to
        the application by means of an argument in the function
        signature. The aggregation of dataReceivePointByArgument is
        subject to variability with the purpose to support the
        conditional existence of sender receiver PortPrototype or the
        variant existence of data receive points in the implementation.
        The upper multiplicity of this role has been increased to * due
        to resolving an atpVariation stereotype. The previous value was
        -1.
    :ivar data_receive_point_by_values: RunnableEntity has explicit read
        access to dataElement of a sender-receiver PortPrototype or nv
        data of a nv data PortPrototype. The result is passed back to
        the application by means of the return value. The aggregation of
        dataReceivePointByValue is subject to variability with the
        purpose to support the conditional existence of sender receiver
        ports or the variant existence of data receive points in the
        implementation. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar data_send_points: RunnableEntity has explicit write access to
        dataElement of a sender-receiver PortPrototype or nv data of a
        nv data PortPrototype. The aggregation of dataSendPoint is
        subject to variability with the purpose to support the
        conditional existence of sender receiver PortPrototype or the
        variant existence of data send points in the implementation. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar data_write_accesss: RunnableEntity has implicit write access
        to dataElement of a sender-receiver PortPrototype or nv data of
        a nv data PortPrototype. The aggregation of dataWriteAccess is
        subject to variability with the purpose to support the
        conditional existence of sender receiver ports or the variant
        existence of dataWriteAccess in the implementation. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar external_triggering_points: The aggregation of
        ExternalTriggeringPoint is subject to variability with the
        purpose to support the conditional existence of trigger ports or
        the variant existence of external triggering points in the
        implementation. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar internal_triggering_points: The aggregation of
        InternalTriggeringPoint is subject to variability with the
        purpose to support the variant existence of internal triggering
        points in the implementation. The upper multiplicity of this
        role has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
    :ivar mode_access_points: The runnable has a mode access point. The
        aggregation of ModeAccessPoint is subject to variability with
        the purpose to support the conditional existence of mode ports
        or the variant existence of mode access points in the
        implementation. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar mode_switch_points: The runnable has a mode switch point. The
        aggregation of ModeSwitchPoint is subject to variability with
        the purpose to support the conditional existence of mode ports
        or the variant existence of mode switch points in the
        implementation. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar parameter_accesss: The presence of a ParameterAccess implies
        that a RunnableEntity needs read only access to a
        ParameterDataPrototype which may either be local or within a
        PortPrototype. The aggregation of ParameterAccess is subject to
        variability with the purpose to support the conditional
        existence of parameter ports and component local parameters as
        well as the variant existence of ParameterAccess (points) in the
        implementation. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar read_local_variables: The presence of a readLocalVariable
        implies that a RunnableEntity needs read access to a
        VariableDataPrototype in the role of
        implicitInterRunnableVariable or explicitInterRunnableVariable.
        The aggregation of readLocalVariable is subject to variability
        with the purpose to support the conditional existence of
        implicitInterRunnableVariable and explicitInterRunnableVariable
        or the variant existence of readLocalVariable (points) in the
        implementation. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar server_call_points: The RunnableEntity has a ServerCallPoint.
        The aggregation of ServerCallPoint is subject to variability
        with the purpose to support the conditional existence of client
        server PortPrototypes or the variant existence of server call
        points in the implementation. The upper multiplicity of this
        role has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
    :ivar symbol: The symbol describing this RunnableEntity's entry
        point. This is considered the API of the RunnableEntity and is
        required during the RTE contract phase.
    :ivar wait_points: The WaitPoint associated with the RunnableEntity.
    :ivar written_local_variables: The presence of a
        writtenLocalVariable implies that a RunnableEntity needs write
        access to a VariableDataPrototype in the role of
        implicitInterRunnableVariable or explicitInterRunnableVariable.
        The aggregation of writtenLocalVariable is subject to
        variability with the purpose to support the conditional
        existence of implicitInterRunnableVariable and
        explicitInterRunnableVariable or the variant existence of
        writtenLocalVariable (points) in the implementation. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
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
        name = "RUNNABLE-ENTITY"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["RunnableEntity.ShortNameFragments"] = (
        field(
            default=None,
            metadata={
                "name": "SHORT-NAME-FRAGMENTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
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
    annotations: Optional["RunnableEntity.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    activation_reasons: Optional["RunnableEntity.ActivationReasons"] = field(
        default=None,
        metadata={
            "name": "ACTIVATION-REASONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    can_enter_exclusive_area_refs: Optional[
        "RunnableEntity.CanEnterExclusiveAreaRefs"
    ] = field(
        default=None,
        metadata={
            "name": "CAN-ENTER-EXCLUSIVE-AREA-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    exclusive_area_nesting_order_refs: Optional[
        "RunnableEntity.ExclusiveAreaNestingOrderRefs"
    ] = field(
        default=None,
        metadata={
            "name": "EXCLUSIVE-AREA-NESTING-ORDER-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    minimum_start_interval: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "MINIMUM-START-INTERVAL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    reentrancy_level: Optional[ReentrancyLevelEnum] = field(
        default=None,
        metadata={
            "name": "REENTRANCY-LEVEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    runs_inside_exclusive_area_refs: Optional[
        "RunnableEntity.RunsInsideExclusiveAreaRefs"
    ] = field(
        default=None,
        metadata={
            "name": "RUNS-INSIDE-EXCLUSIVE-AREA-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_addr_method_ref: Optional["RunnableEntity.SwAddrMethodRef"] = field(
        default=None,
        metadata={
            "name": "SW-ADDR-METHOD-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    arguments: Optional["RunnableEntity.Arguments"] = field(
        default=None,
        metadata={
            "name": "ARGUMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    asynchronous_server_call_result_points: Optional[
        "RunnableEntity.AsynchronousServerCallResultPoints"
    ] = field(
        default=None,
        metadata={
            "name": "ASYNCHRONOUS-SERVER-CALL-RESULT-POINTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    can_be_invoked_concurrently: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "CAN-BE-INVOKED-CONCURRENTLY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_read_accesss: Optional["RunnableEntity.DataReadAccesss"] = field(
        default=None,
        metadata={
            "name": "DATA-READ-ACCESSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_receive_point_by_arguments: Optional[
        "RunnableEntity.DataReceivePointByArguments"
    ] = field(
        default=None,
        metadata={
            "name": "DATA-RECEIVE-POINT-BY-ARGUMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_receive_point_by_values: Optional[
        "RunnableEntity.DataReceivePointByValues"
    ] = field(
        default=None,
        metadata={
            "name": "DATA-RECEIVE-POINT-BY-VALUES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_send_points: Optional["RunnableEntity.DataSendPoints"] = field(
        default=None,
        metadata={
            "name": "DATA-SEND-POINTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_write_accesss: Optional["RunnableEntity.DataWriteAccesss"] = field(
        default=None,
        metadata={
            "name": "DATA-WRITE-ACCESSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    external_triggering_points: Optional[
        "RunnableEntity.ExternalTriggeringPoints"
    ] = field(
        default=None,
        metadata={
            "name": "EXTERNAL-TRIGGERING-POINTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    internal_triggering_points: Optional[
        "RunnableEntity.InternalTriggeringPoints"
    ] = field(
        default=None,
        metadata={
            "name": "INTERNAL-TRIGGERING-POINTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mode_access_points: Optional["RunnableEntity.ModeAccessPoints"] = field(
        default=None,
        metadata={
            "name": "MODE-ACCESS-POINTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mode_switch_points: Optional["RunnableEntity.ModeSwitchPoints"] = field(
        default=None,
        metadata={
            "name": "MODE-SWITCH-POINTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    parameter_accesss: Optional["RunnableEntity.ParameterAccesss"] = field(
        default=None,
        metadata={
            "name": "PARAMETER-ACCESSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    read_local_variables: Optional["RunnableEntity.ReadLocalVariables"] = (
        field(
            default=None,
            metadata={
                "name": "READ-LOCAL-VARIABLES",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    server_call_points: Optional["RunnableEntity.ServerCallPoints"] = field(
        default=None,
        metadata={
            "name": "SERVER-CALL-POINTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    symbol: Optional[CIdentifier] = field(
        default=None,
        metadata={
            "name": "SYMBOL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    wait_points: Optional["RunnableEntity.WaitPoints"] = field(
        default=None,
        metadata={
            "name": "WAIT-POINTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    written_local_variables: Optional[
        "RunnableEntity.WrittenLocalVariables"
    ] = field(
        default=None,
        metadata={
            "name": "WRITTEN-LOCAL-VARIABLES",
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
    class ActivationReasons:
        executable_entity_activation_reason: list[
            ExecutableEntityActivationReason
        ] = field(
            default_factory=list,
            metadata={
                "name": "EXECUTABLE-ENTITY-ACTIVATION-REASON",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class CanEnterExclusiveAreaRefs:
        can_enter_exclusive_area_ref: list[
            "RunnableEntity.CanEnterExclusiveAreaRefs.CanEnterExclusiveAreaRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "CAN-ENTER-EXCLUSIVE-AREA-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class CanEnterExclusiveAreaRef(Ref):
            dest: Optional[ExclusiveAreaSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class ExclusiveAreaNestingOrderRefs:
        exclusive_area_nesting_order_ref: list[
            "RunnableEntity.ExclusiveAreaNestingOrderRefs.ExclusiveAreaNestingOrderRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "EXCLUSIVE-AREA-NESTING-ORDER-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ExclusiveAreaNestingOrderRef(Ref):
            dest: Optional[ExclusiveAreaNestingOrderSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class RunsInsideExclusiveAreaRefs:
        runs_inside_exclusive_area_ref: list[
            "RunnableEntity.RunsInsideExclusiveAreaRefs.RunsInsideExclusiveAreaRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "RUNS-INSIDE-EXCLUSIVE-AREA-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class RunsInsideExclusiveAreaRef(Ref):
            dest: Optional[ExclusiveAreaSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class SwAddrMethodRef(Ref):
        dest: Optional[SwAddrMethodSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class Arguments:
        runnable_entity_argument: list[RunnableEntityArgument] = field(
            default_factory=list,
            metadata={
                "name": "RUNNABLE-ENTITY-ARGUMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class AsynchronousServerCallResultPoints:
        asynchronous_server_call_result_point: list[
            AsynchronousServerCallResultPoint
        ] = field(
            default_factory=list,
            metadata={
                "name": "ASYNCHRONOUS-SERVER-CALL-RESULT-POINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class DataReadAccesss:
        variable_access: list[VariableAccess] = field(
            default_factory=list,
            metadata={
                "name": "VARIABLE-ACCESS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class DataReceivePointByArguments:
        variable_access: list[VariableAccess] = field(
            default_factory=list,
            metadata={
                "name": "VARIABLE-ACCESS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class DataReceivePointByValues:
        variable_access: list[VariableAccess] = field(
            default_factory=list,
            metadata={
                "name": "VARIABLE-ACCESS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class DataSendPoints:
        variable_access: list[VariableAccess] = field(
            default_factory=list,
            metadata={
                "name": "VARIABLE-ACCESS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class DataWriteAccesss:
        variable_access: list[VariableAccess] = field(
            default_factory=list,
            metadata={
                "name": "VARIABLE-ACCESS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ExternalTriggeringPoints:
        external_triggering_point: list[ExternalTriggeringPoint] = field(
            default_factory=list,
            metadata={
                "name": "EXTERNAL-TRIGGERING-POINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class InternalTriggeringPoints:
        internal_triggering_point: list[InternalTriggeringPoint] = field(
            default_factory=list,
            metadata={
                "name": "INTERNAL-TRIGGERING-POINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ModeAccessPoints:
        mode_access_point: list[ModeAccessPoint] = field(
            default_factory=list,
            metadata={
                "name": "MODE-ACCESS-POINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ModeSwitchPoints:
        mode_switch_point: list[ModeSwitchPoint] = field(
            default_factory=list,
            metadata={
                "name": "MODE-SWITCH-POINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ParameterAccesss:
        parameter_access: list[ParameterAccess] = field(
            default_factory=list,
            metadata={
                "name": "PARAMETER-ACCESS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ReadLocalVariables:
        variable_access: list[VariableAccess] = field(
            default_factory=list,
            metadata={
                "name": "VARIABLE-ACCESS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ServerCallPoints:
        asynchronous_server_call_point: list[AsynchronousServerCallPoint] = (
            field(
                default_factory=list,
                metadata={
                    "name": "ASYNCHRONOUS-SERVER-CALL-POINT",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        synchronous_server_call_point: list[SynchronousServerCallPoint] = (
            field(
                default_factory=list,
                metadata={
                    "name": "SYNCHRONOUS-SERVER-CALL-POINT",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )

    @dataclass
    class WaitPoints:
        wait_point: list[WaitPoint] = field(
            default_factory=list,
            metadata={
                "name": "WAIT-POINT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class WrittenLocalVariables:
        variable_access: list[VariableAccess] = field(
            default_factory=list,
            metadata={
                "name": "VARIABLE-ACCESS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
