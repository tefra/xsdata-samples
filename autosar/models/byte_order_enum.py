from dataclasses import dataclass, field
from typing import Optional
from .byte_order_enum_simple import ByteOrderEnumSimple

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ByteOrderEnum:
    """When more than one byte is stored in the memory the order of those bytes
    may differ depending on the architecture of the processing unit.

    If the least significant byte is stored at the lowest address, this
    architecture is called little endian and otherwise it is called big
    endian. ByteOrder is very important in case of communication between
    different PUs or ECUs.

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
        name = "BYTE-ORDER-ENUM"

    value: Optional[ByteOrderEnumSimple] = field(
        default=None,
        metadata={
            "required": True,
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
