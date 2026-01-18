from __future__ import annotations

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
from .system_signal_subtypes_enum import SystemSignalSubtypesEnum
from .text_table_mapping import TextTableMapping
from .variable_data_prototype_in_system_instance_ref import (
    VariableDataPrototypeInSystemInstanceRef,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SenderReceiverToSignalMapping:
    """
    Mapping of a sender receiver communication data element to a signal.

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
    :ivar data_element_iref: Reference to the data element.
    :ivar sender_to_signal_text_table_mapping: This mapping allows for
        the text-table translation between the sending DataPrototype
        that is defined in the PortPrototype and the physicalProps
        defined for the SystemSignal.
    :ivar signal_to_receiver_text_table_mapping: This mapping allows for
        the text-table translation between the physicalProps defined for
        the SystemSignal and a receiving DataPrototype that is defined
        in the PortPrototype.
    :ivar system_signal_ref: Reference to the system signal used to
        carry the data element.
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
        name = "SENDER-RECEIVER-TO-SIGNAL-MAPPING"

    communication_direction: CommunicationDirectionType | None = field(
        default=None,
        metadata={
            "name": "COMMUNICATION-DIRECTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_group_refs: SenderReceiverToSignalMapping.EventGroupRefs | None = field(
        default=None,
        metadata={
            "name": "EVENT-GROUP-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_handler_refs: SenderReceiverToSignalMapping.EventHandlerRefs | None = field(
        default=None,
        metadata={
            "name": "EVENT-HANDLER-REFS",
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
    service_instance_refs: SenderReceiverToSignalMapping.ServiceInstanceRefs | None = field(
        default=None,
        metadata={
            "name": "SERVICE-INSTANCE-REFS",
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
    data_element_iref: VariableDataPrototypeInSystemInstanceRef | None = (
        field(
            default=None,
            metadata={
                "name": "DATA-ELEMENT-IREF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    sender_to_signal_text_table_mapping: TextTableMapping | None = field(
        default=None,
        metadata={
            "name": "SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    signal_to_receiver_text_table_mapping: TextTableMapping | None = field(
        default=None,
        metadata={
            "name": "SIGNAL-TO-RECEIVER-TEXT-TABLE-MAPPING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    system_signal_ref: SenderReceiverToSignalMapping.SystemSignalRef | None = field(
        default=None,
        metadata={
            "name": "SYSTEM-SIGNAL-REF",
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

    @dataclass
    class EventGroupRefs:
        event_group_ref: list[
            SenderReceiverToSignalMapping.EventGroupRefs.EventGroupRef
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
            dest: ConsumedEventGroupSubtypesEnum | None = field(
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
            SenderReceiverToSignalMapping.EventHandlerRefs.EventHandlerRef
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
            dest: EventHandlerSubtypesEnum | None = field(
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
            SenderReceiverToSignalMapping.ServiceInstanceRefs.ServiceInstanceRef
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
            dest: AbstractServiceInstanceSubtypesEnum | None = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class SystemSignalRef(Ref):
        dest: SystemSignalSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
