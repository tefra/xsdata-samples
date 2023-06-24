from dataclasses import dataclass, field
from typing import Optional
from .integer import Integer

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwBitRepresentation:
    """Description of the structure of a bit variable: Comprises of the bitPosition in a memory object (e.g. swHostVariable, which stands parallel to swBitRepresentation) and the numberOfBits . In this way, interrelated memory areas can be described. Non-related memory areas are not supported.

    :ivar bit_position: If the "bit data object" is hosted within
        another data object (e.g. if the memory can be accessed via byte
        as well as bit address), this attribute specifies the position
        of the data object. The count starts at zero (0).
    :ivar number_of_bits: Number of bits allocated by a "bit data
        object" within its host data object.
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
        name = "SW-BIT-REPRESENTATION"

    bit_position: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "BIT-POSITION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    number_of_bits: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "NUMBER-OF-BITS",
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
