from __future__ import annotations

from dataclasses import dataclass, field

from .boolean import Boolean
from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class TpPort:
    """
    Dynamic or direct assignment of a PortNumber.

    :ivar dynamically_assigned: Indicates whether the source port is
        dynamically assigned.
    :ivar port_number: Port Number.
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
        name = "TP-PORT"

    dynamically_assigned: None | Boolean = field(
        default=None,
        metadata={
            "name": "DYNAMICALLY-ASSIGNED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    port_number: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "PORT-NUMBER",
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
