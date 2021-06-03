from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SecOcJobSemanticEnumSimple(Enum):
    """
    :cvar AUTHENTICATE: Authentication algorithm for Authenticator
        generation/verification.
    :cvar VERIFY: Asymmetric cryptographic algorithm to generate/verify
        a signature
    """
    AUTHENTICATE = "AUTHENTICATE"
    VERIFY = "VERIFY"
