from dataclasses import dataclass, field
from typing import Optional

from .udp_collection_trigger_enum_simple import UdpCollectionTriggerEnumSimple

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class UdpCollectionTriggerEnum:
    """
    Defines whether the ServiceInterface element (event or method)
    contributes to the triggering of the udp data transmission if data
    collection is enabled.

    :ivar value:
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
        name = "UDP-COLLECTION-TRIGGER-ENUM"

    value: UdpCollectionTriggerEnumSimple | None = field(
        default=None,
        metadata={
            "required": True,
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
