from dataclasses import dataclass, field
from typing import Optional

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
from .ref import Ref
from .sender_rec_array_element_mapping import (
    SenderRecArrayTypeMapping,
    SenderRecRecordTypeMapping,
)
from .system_signal_group_subtypes_enum import SystemSignalGroupSubtypesEnum
from .variable_data_prototype_in_system_instance_ref import (
    VariableDataPrototypeInSystemInstanceRef,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SenderReceiverToSignalGroupMapping:
    """
    Mapping of a sender receiver communication data element with a
    composite datatype to a signal group.

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
    :ivar data_element_iref: Reference to a data element with a
        composite datatype which is mapped to a signal group.
    :ivar signal_group_ref: Reference to the signal group, which contain
        all primitive datatypes of the composite type
    :ivar type_mapping: The CompositeTypeMapping maps the
        ApplicationArrayElements and ApplicationRecordElements to
        Signals of the SignalGroup.
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
        name = "SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING"

    communication_direction: Optional[CommunicationDirectionType] = field(
        default=None,
        metadata={
            "name": "COMMUNICATION-DIRECTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_group_refs: Optional[
        "SenderReceiverToSignalGroupMapping.EventGroupRefs"
    ] = field(
        default=None,
        metadata={
            "name": "EVENT-GROUP-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_handler_refs: Optional[
        "SenderReceiverToSignalGroupMapping.EventHandlerRefs"
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
        "SenderReceiverToSignalGroupMapping.ServiceInstanceRefs"
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
    data_element_iref: Optional[VariableDataPrototypeInSystemInstanceRef] = (
        field(
            default=None,
            metadata={
                "name": "DATA-ELEMENT-IREF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    signal_group_ref: Optional[
        "SenderReceiverToSignalGroupMapping.SignalGroupRef"
    ] = field(
        default=None,
        metadata={
            "name": "SIGNAL-GROUP-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    type_mapping: Optional[
        "SenderReceiverToSignalGroupMapping.TypeMapping"
    ] = field(
        default=None,
        metadata={
            "name": "TYPE-MAPPING",
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
            "SenderReceiverToSignalGroupMapping.EventGroupRefs.EventGroupRef"
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
            "SenderReceiverToSignalGroupMapping.EventHandlerRefs.EventHandlerRef"
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
            "SenderReceiverToSignalGroupMapping.ServiceInstanceRefs.ServiceInstanceRef"
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
    class SignalGroupRef(Ref):
        dest: Optional[SystemSignalGroupSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TypeMapping:
        sender_rec_array_type_mapping: Optional[SenderRecArrayTypeMapping] = (
            field(
                default=None,
                metadata={
                    "name": "SENDER-REC-ARRAY-TYPE-MAPPING",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        sender_rec_record_type_mapping: Optional[
            SenderRecRecordTypeMapping
        ] = field(
            default=None,
            metadata={
                "name": "SENDER-REC-RECORD-TYPE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
