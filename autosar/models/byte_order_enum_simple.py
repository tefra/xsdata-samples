from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ByteOrderEnumSimple(Enum):
    """
    :cvar MOST_SIGNIFICANT_BYTE_FIRST: Most significant byte shall come
        at the lowest address (also known as BigEndian or as Motorola-
        Format)
    :cvar MOST_SIGNIFICANT_BYTE_LAST: Most significant byte shall come
        highest address (also known as LittleEndian or as Intel-Format)
    :cvar OPAQUE: For opaque data endianness conversion has to be
        configured to Opaque. See AUTOSAR COM Specification for more
        details.
    """

    MOST_SIGNIFICANT_BYTE_FIRST = "MOST-SIGNIFICANT-BYTE-FIRST"
    MOST_SIGNIFICANT_BYTE_LAST = "MOST-SIGNIFICANT-BYTE-LAST"
    OPAQUE = "OPAQUE"
