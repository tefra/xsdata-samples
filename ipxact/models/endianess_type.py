from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class EndianessType(Enum):
    """'big': means the most significant element of any multi-element  data field
    is stored at the lowest memory address.

    'little' means the least significant element of any multi-element
    data field is stored at the lowest memory address. If this element
    is not present the default is 'little' endian.
    """

    BIG = "big"
    LITTLE = "little"
