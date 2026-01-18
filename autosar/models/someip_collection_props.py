from __future__ import annotations

from dataclasses import dataclass, field

from .time_value import TimeValue
from .udp_collection_trigger_enum import UdpCollectionTriggerEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SomeipCollectionProps:
    """
    Collection of attributes that are configurable for an event that is
    provided by a ServiceInstance or for a method that is provided or
    requested by a ServiceInstance.

    :ivar udp_collection_buffer_timeout: Maximum time, an outgoing
        message (event, method call or method response) may be delayed,
        due to data collection.
    :ivar udp_collection_trigger: Defines whether the ServiceInterface
        element (event or method) contributes to the triggering of the
        udp data transmission if data collection is enabled.
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
        name = "SOMEIP-COLLECTION-PROPS"

    udp_collection_buffer_timeout: None | TimeValue = field(
        default=None,
        metadata={
            "name": "UDP-COLLECTION-BUFFER-TIMEOUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    udp_collection_trigger: None | UdpCollectionTriggerEnum = field(
        default=None,
        metadata={
            "name": "UDP-COLLECTION-TRIGGER",
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
