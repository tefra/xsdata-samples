from dataclasses import dataclass, field
from typing import Optional

from .support_buffer_locking_enum import SupportBufferLockingEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CommunicationBufferLocking:
    """
    The aggregation of this meta-class specifies that a RunnableEntity
    supports locked communication buffers supplied by the RTE.

    It is able to cope with the error RTE_E_COM_BUSY.

    :ivar support_buffer_locking: This attribute is used to indicate the
        intended buffer locking behavior.
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
        name = "COMMUNICATION-BUFFER-LOCKING"

    support_buffer_locking: Optional[SupportBufferLockingEnum] = field(
        default=None,
        metadata={
            "name": "SUPPORT-BUFFER-LOCKING",
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
