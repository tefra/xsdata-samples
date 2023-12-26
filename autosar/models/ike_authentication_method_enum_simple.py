from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class IkeAuthenticationMethodEnumSimple(Enum):
    """
    :cvar DSA: Digital Signature Authentication
    :cvar PSK: Pre-shared key authentication
    """

    DSA = "DSA"
    PSK = "PSK"
