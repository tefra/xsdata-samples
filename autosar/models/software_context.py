from dataclasses import dataclass, field
from typing import Optional
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SoftwareContext:
    """
    Specifies the context of the software for this resource consumption.

    :ivar input: Specifies the input vector which is used to provide the
        ExecutionTime.
    :ivar state: Specifies the state the software is in when the
        ExecutionTime is provided.
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
        name = "SOFTWARE-CONTEXT"

    input: Optional[String] = field(
        default=None,
        metadata={
            "name": "INPUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    state: Optional[String] = field(
        default=None,
        metadata={
            "name": "STATE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )
