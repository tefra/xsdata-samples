from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TlsVersionEnumSimple(Enum):
    """
    :cvar LTS_13: TLS version 1.3
    :cvar TLS_12: TLS version 1.2
    :cvar TLS_13: TLS version 1.3
    """
    LTS_13 = "LTS-13"
    TLS_12 = "TLS-12"
    TLS_13 = "TLS-13"
