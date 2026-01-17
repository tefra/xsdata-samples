from enum import Enum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


class SimpleCodeDataType(Enum):
    """
    SimpleCodeDataType restricts SimpleDataType to specify the allowable
    data types for a simple code.

    The possible values are simply Alpha, AlphaNumeric, or Numeric.

    :cvar ALPHA: A string datatype which only allows for the simple
        aplhabetic charcter set of A-Z, a-z.
    :cvar ALPHA_NUMERIC: A string datatype which only allows for the
        simple alphabetic character set of A-Z, a-z plus the simple
        numeric character set of 0-9.
    :cvar NUMERIC: A string datatype which only allows for the simple
        numeric character set of 0-9. This format is not treated as an
        integer, and therefore can having leading zeros.
    """

    ALPHA = "Alpha"
    ALPHA_NUMERIC = "AlphaNumeric"
    NUMERIC = "Numeric"
