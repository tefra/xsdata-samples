from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.unsigned_bit_vector_expression import (
    UnsignedBitVectorExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class WriteValueConstraintType:
    """
    A constraint on the values that can be written to this field.

    Absence of this element implies that any value that fits can be written
    to it.

    :ivar write_as_read: writeAsRead indicates that only a value
        immediately read before a write is a legal value to be written.
    :ivar use_enumerated_values: useEnumeratedValues indicates that only
        write enumeration value shall be legal values to be written.
    :ivar minimum: The minimum legal value that may be written to a
        field
    :ivar maximum: The maximum legal value that may be written to a
        field
    """

    class Meta:
        name = "writeValueConstraintType"

    write_as_read: bool | None = field(
        default=None,
        metadata={
            "name": "writeAsRead",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    use_enumerated_values: bool | None = field(
        default=None,
        metadata={
            "name": "useEnumeratedValues",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    minimum: UnsignedBitVectorExpression | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    maximum: UnsignedBitVectorExpression | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
