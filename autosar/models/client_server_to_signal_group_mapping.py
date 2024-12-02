from dataclasses import dataclass, field
from typing import Optional

from .abstract_service_instance_subtypes_enum import (
    AbstractServiceInstanceSubtypesEnum,
)
from .admin_data import (
    DocumentationBlock,
    VariationPoint,
)
from .application_error_mapping import ApplicationErrorMapping
from .client_id_mapping import ClientIdMapping
from .client_server_array_element_mapping import (
    ClientServerArrayTypeMapping,
    ClientServerRecordTypeMapping,
)
from .client_server_primitive_type_mapping import (
    ClientServerPrimitiveTypeMapping,
)
from .communication_direction_type import CommunicationDirectionType
from .consumed_event_group_subtypes_enum import ConsumedEventGroupSubtypesEnum
from .empty_signal_mapping import EmptySignalMapping
from .event_handler_subtypes_enum import EventHandlerSubtypesEnum
from .operation_in_system_instance_ref import OperationInSystemInstanceRef
from .ref import Ref
from .sequence_counter_mapping import SequenceCounterMapping
from .system_signal_group_subtypes_enum import SystemSignalGroupSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ClientServerToSignalGroupMapping:
    """This mapping is deprecated and will be removed in future.

    It is replaced by the ClientServerToSignalMapping.
    Old description:
    Mapping of client server operation arguments to signals of a signal group. Arguments with a primitive datatype will be mapped via the "ClientServerPrimitiveTypeMapping" element.
    Arguments with composite datatypes will be mapped via the "CompositeTypeMapping" element.

    :ivar communication_direction: This attribute controls the direction
        into which the mapped SystemSignal is communicated with respect
        to the kind of PortPrototype used as the context element of the
        DataMapping.
    :ivar event_group_refs: Via this reference a connection between the
        VFB View and the Ethernet EventGroups can be created.
    :ivar event_handler_refs: Via this reference a connection between
        the VFB View and the Ethernet EventHandlers can be created.
    :ivar introduction: This represents introductory documentation about
        the data mapping.
    :ivar service_instance_refs: Via this reference a connection between
        the VFB View and the Ethernet Services can be created.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar application_error: In client server communication, the server
        may return any value within the application error range.
    :ivar client_id: In case of a server on one ECU with multiple
        clients on other ECUs, the client server communication shall use
        different unique COM signals and signal groups for each client
        to allow the identification of the client associated with each
        system signal.
    :ivar composite_type_mappings: Mapping of arguments with composite
        datatypes.
    :ivar empty_signal: An emptySignal is created if no actual data is
        configured for a client-server communication, but if the RTE
        shall send a SignalGroup to initiate the communication. An
        EmptySignalMapping shall only reference a SystemSignal that is
        referenced by an ISignal with length equal to zero.
    :ivar mapped_operation_iref: Reference to a Operation, which is
        mapped to a signal group.
    :ivar primitive_type_mappings: Mapping of an argument with a
        primitive datatype to a signal.
    :ivar request_group_ref: Reference to the signal group which
        contains the references to request signals used to transport the
        IN and INOUT arguments of the operation.
    :ivar response_group_ref: Reference to the signal group which
        contains the references to response signals used to transport
        the OUT and INOUT arguments of the operation.
    :ivar sequence_counter: The purpose of sequence counters is to map a
        response to the correct request of a known client.
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
    """

    class Meta:
        name = "CLIENT-SERVER-TO-SIGNAL-GROUP-MAPPING"

    communication_direction: Optional[CommunicationDirectionType] = field(
        default=None,
        metadata={
            "name": "COMMUNICATION-DIRECTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_group_refs: Optional[
        "ClientServerToSignalGroupMapping.EventGroupRefs"
    ] = field(
        default=None,
        metadata={
            "name": "EVENT-GROUP-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_handler_refs: Optional[
        "ClientServerToSignalGroupMapping.EventHandlerRefs"
    ] = field(
        default=None,
        metadata={
            "name": "EVENT-HANDLER-REFS",
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
    service_instance_refs: Optional[
        "ClientServerToSignalGroupMapping.ServiceInstanceRefs"
    ] = field(
        default=None,
        metadata={
            "name": "SERVICE-INSTANCE-REFS",
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
    application_error: Optional[ApplicationErrorMapping] = field(
        default=None,
        metadata={
            "name": "APPLICATION-ERROR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    client_id: Optional[ClientIdMapping] = field(
        default=None,
        metadata={
            "name": "CLIENT-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    composite_type_mappings: Optional[
        "ClientServerToSignalGroupMapping.CompositeTypeMappings"
    ] = field(
        default=None,
        metadata={
            "name": "COMPOSITE-TYPE-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    empty_signal: Optional[EmptySignalMapping] = field(
        default=None,
        metadata={
            "name": "EMPTY-SIGNAL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mapped_operation_iref: Optional[OperationInSystemInstanceRef] = field(
        default=None,
        metadata={
            "name": "MAPPED-OPERATION-IREF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    primitive_type_mappings: Optional[
        "ClientServerToSignalGroupMapping.PrimitiveTypeMappings"
    ] = field(
        default=None,
        metadata={
            "name": "PRIMITIVE-TYPE-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    request_group_ref: Optional[
        "ClientServerToSignalGroupMapping.RequestGroupRef"
    ] = field(
        default=None,
        metadata={
            "name": "REQUEST-GROUP-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    response_group_ref: Optional[
        "ClientServerToSignalGroupMapping.ResponseGroupRef"
    ] = field(
        default=None,
        metadata={
            "name": "RESPONSE-GROUP-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sequence_counter: Optional[SequenceCounterMapping] = field(
        default=None,
        metadata={
            "name": "SEQUENCE-COUNTER",
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

    @dataclass
    class EventGroupRefs:
        event_group_ref: list[
            "ClientServerToSignalGroupMapping.EventGroupRefs.EventGroupRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "EVENT-GROUP-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class EventGroupRef(Ref):
            dest: Optional[ConsumedEventGroupSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class EventHandlerRefs:
        event_handler_ref: list[
            "ClientServerToSignalGroupMapping.EventHandlerRefs.EventHandlerRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "EVENT-HANDLER-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class EventHandlerRef(Ref):
            dest: Optional[EventHandlerSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class ServiceInstanceRefs:
        service_instance_ref: list[
            "ClientServerToSignalGroupMapping.ServiceInstanceRefs.ServiceInstanceRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "SERVICE-INSTANCE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ServiceInstanceRef(Ref):
            dest: Optional[AbstractServiceInstanceSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class CompositeTypeMappings:
        client_server_array_type_mapping: list[
            ClientServerArrayTypeMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "CLIENT-SERVER-ARRAY-TYPE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        client_server_record_type_mapping: list[
            ClientServerRecordTypeMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "CLIENT-SERVER-RECORD-TYPE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class PrimitiveTypeMappings:
        client_server_primitive_type_mapping: list[
            ClientServerPrimitiveTypeMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "CLIENT-SERVER-PRIMITIVE-TYPE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class RequestGroupRef(Ref):
        dest: Optional[SystemSignalGroupSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ResponseGroupRef(Ref):
        dest: Optional[SystemSignalGroupSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
