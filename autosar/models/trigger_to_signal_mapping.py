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
from .ref import Ref
from .system_signal_subtypes_enum import SystemSignalSubtypesEnum
from .trigger_in_system_instance_ref import TriggerInSystemInstanceRef

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class TriggerToSignalMapping:
    """
    This meta-class represents the ability to map a trigger to a
    SystemSignal of size 0.

    The Trigger does not transport any other information than its
    existence, therefore the limitation in terms of signal length.

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
    :ivar trigger_iref: This represents the Trigger that shall be used
        to trigger RunnableEntities deployed to a remote ECU.
    :ivar system_signal_ref: This is the SystemSignal taken to transport
        the Trigger over the network.
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
        name = "TRIGGER-TO-SIGNAL-MAPPING"

    communication_direction: None | CommunicationDirectionType = field(
        default=None,
        metadata={
            "name": "COMMUNICATION-DIRECTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_group_refs: None | TriggerToSignalMapping.EventGroupRefs = field(
        default=None,
        metadata={
            "name": "EVENT-GROUP-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_handler_refs: None | TriggerToSignalMapping.EventHandlerRefs = field(
        default=None,
        metadata={
            "name": "EVENT-HANDLER-REFS",
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
    service_instance_refs: (
        None | TriggerToSignalMapping.ServiceInstanceRefs
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
    trigger_iref: None | TriggerInSystemInstanceRef = field(
        default=None,
        metadata={
            "name": "TRIGGER-IREF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    system_signal_ref: None | TriggerToSignalMapping.SystemSignalRef = field(
        default=None,
        metadata={
            "name": "SYSTEM-SIGNAL-REF",
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
            TriggerToSignalMapping.EventGroupRefs.EventGroupRef
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
            TriggerToSignalMapping.EventHandlerRefs.EventHandlerRef
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
            TriggerToSignalMapping.ServiceInstanceRefs.ServiceInstanceRef
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
    class SystemSignalRef(Ref):
        dest: SystemSignalSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
