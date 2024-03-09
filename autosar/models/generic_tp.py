from dataclasses import dataclass, field
from typing import Optional

from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class GenericTp:
    """
    Content Model for a generic transport protocol.

    :ivar tp_address: Transport Protocol dependent Address.
    :ivar tp_technology: Name of the used Transport Protocol.
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
        name = "GENERIC-TP"

    tp_address: Optional[String] = field(
        default=None,
        metadata={
            "name": "TP-ADDRESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tp_technology: Optional[String] = field(
        default=None,
        metadata={
            "name": "TP-TECHNOLOGY",
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
