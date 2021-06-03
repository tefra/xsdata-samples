from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class HttpAcceptEncodingEnumSimple(Enum):
    """
    :cvar DEFLATE: Use deflate compression.
    :cvar GZIP: Use gzip pcompression.
    """
    DEFLATE = "DEFLATE"
    GZIP = "GZIP"
