from __future__ import annotations

from dataclasses import dataclass, field

from .abstract_service_instance_subtypes_enum import (
    AbstractServiceInstanceSubtypesEnum,
)
from .admin_data import (
    DocumentationBlock,
    VariationPoint,
)
from .communication_direction_type import CommunicationDirectionType
from .consumed_event_group_subtypes_enum import ConsumedEventGroupSubtypesEnum
from .event_handler_subtypes_enum import EventHandlerSubtypesEnum
from .operation_in_system_instance_ref import OperationInSystemInstanceRef
from .positive_integer import PositiveInteger
from .ref import Ref
from .serialization_technology_subtypes_enum import (
    SerializationTechnologySubtypesEnum,
)
from .system_signal_subtypes_enum import SystemSignalSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class ClientServerToSignalMapping:
    """
    This element maps the ClientServerOperation to call- and
    return-SystemSignals.

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
    :ivar call_signal_ref: Reference to the callSignal to which the IN
        and INOUT ArgumentDataPrototypes are mapped.
    :ivar client_server_operation_iref: Reference to a
        ClientServerOperation, which is mapped to a call SystemSignal
        and a return SystemSignal.
    :ivar length_client_id: This attribute defines the length of the
        used client identifier in bits.  If the attribute does not exist
        or its value is set to 0 this means that the client identifier
        is not used. Please note that this attribute is deprecated and
        will be removed in future (Value is fixed to UInt16).
    :ivar length_sequence_counter: The purpose of a sequence counter is
        to map a response to the correct request of a known client. This
        attribute describes the length of the used sequence counter in
        bits. If the attribute does not exist or its value is set to 0
        this means that the sequence counter is not used. Please note
        that this attribute is deprecated and will be removed in future
        (Value is fixed to UInt16).
    :ivar return_signal_ref: Reference to the returnSignal to which the
        OUT and INOUT ArgumentDataPrototypes are mapped.
    :ivar serializer_ref: The reference is set to obsolete. Use
        ISignal.dataTransformation instead.
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
        name = "CLIENT-SERVER-TO-SIGNAL-MAPPING"

    communication_direction: None | CommunicationDirectionType = field(
        default=None,
        metadata={
            "name": "COMMUNICATION-DIRECTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_group_refs: None | ClientServerToSignalMapping.EventGroupRefs = (
        field(
            default=None,
            metadata={
                "name": "EVENT-GROUP-REFS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    event_handler_refs: None | ClientServerToSignalMapping.EventHandlerRefs = (
        field(
            default=None,
            metadata={
                "name": "EVENT-HANDLER-REFS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    introduction: None | DocumentationBlock = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    service_instance_refs: (
        None | ClientServerToSignalMapping.ServiceInstanceRefs
    ) = field(
        default=None,
        metadata={
            "name": "SERVICE-INSTANCE-REFS",
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
    call_signal_ref: None | ClientServerToSignalMapping.CallSignalRef = field(
        default=None,
        metadata={
            "name": "CALL-SIGNAL-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    client_server_operation_iref: None | OperationInSystemInstanceRef = field(
        default=None,
        metadata={
            "name": "CLIENT-SERVER-OPERATION-IREF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    length_client_id: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "LENGTH-CLIENT-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    length_sequence_counter: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "LENGTH-SEQUENCE-COUNTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    return_signal_ref: None | ClientServerToSignalMapping.ReturnSignalRef = (
        field(
            default=None,
            metadata={
                "name": "RETURN-SIGNAL-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    serializer_ref: None | ClientServerToSignalMapping.SerializerRef = field(
        default=None,
        metadata={
            "name": "SERIALIZER-REF",
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

    @dataclass(kw_only=True)
    class EventGroupRefs:
        event_group_ref: list[
            ClientServerToSignalMapping.EventGroupRefs.EventGroupRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "EVENT-GROUP-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass(kw_only=True)
        class EventGroupRef(Ref):
            dest: ConsumedEventGroupSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass(kw_only=True)
    class EventHandlerRefs:
        event_handler_ref: list[
            ClientServerToSignalMapping.EventHandlerRefs.EventHandlerRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "EVENT-HANDLER-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass(kw_only=True)
        class EventHandlerRef(Ref):
            dest: EventHandlerSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass(kw_only=True)
    class ServiceInstanceRefs:
        service_instance_ref: list[
            ClientServerToSignalMapping.ServiceInstanceRefs.ServiceInstanceRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "SERVICE-INSTANCE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass(kw_only=True)
        class ServiceInstanceRef(Ref):
            dest: AbstractServiceInstanceSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass(kw_only=True)
    class CallSignalRef(Ref):
        dest: SystemSignalSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ReturnSignalRef(Ref):
        dest: SystemSignalSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class SerializerRef(Ref):
        dest: SerializationTechnologySubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
