from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class FormatType(Enum):
    """This is an indication on the format of the value.

    bit: 1-bit or more (vector) bits unsigned integer, byte: 8-bit signed integer, shortint: 16-bit signed integer, int: 32-bit signed integer, longint: 64-bit signed integer, shortreal: 32-bit signed floating point number, real: 64-bit signed floating point number, string: textual information.
    """

    BIT = "bit"
    BYTE = "byte"
    SHORTINT = "shortint"
    INT = "int"
    LONGINT = "longint"
    SHORTREAL = "shortreal"
    REAL = "real"
    STRING = "string"
