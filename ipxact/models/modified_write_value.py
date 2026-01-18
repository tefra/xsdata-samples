from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.modified_write_value_type import ModifiedWriteValueType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ModifiedWriteValue:
    """
    If present this element describes the modification of field data caused
    by a write operation. 'oneToClear' means that in a bitwise fashion each
    write data bit of a one will clear the corresponding bit in the field.
    'oneToSet' means that in a bitwise fashion each write data bit of a one
    will set the corresponding bit in the field. 'oneToToggle' means that
    in a bitwise fashion each write data bit of a one will toggle the
    corresponding bit in the field. 'zeroToClear' means that in a bitwise
    fashion each write data bit of a zero will clear the corresponding bit
    in the field. 'zeroToSet' means that in a bitwise fashion each write
    data bit of a zero will set the corresponding bit in the field.
    'zeroToToggle' means that in a bitwise fashion each write data bit of a
    zero will toggle the corresponding bit in the field. 'clear' means any
    write to this field clears the field. 'set' means any write to the
    field sets the field. 'modify' means any write to this field may modify
    that data.

    If this element is not present the write operation data is written.
    """

    class Meta:
        name = "modifiedWriteValue"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    value: ModifiedWriteValueType | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    modify: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
