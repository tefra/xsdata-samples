from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CryptoObjectTypeEnumSimple(Enum):
    """
    :cvar PRIVATE_KEY: cryp::PrivateKey object
    :cvar PUBLIC_KEY: cryp::PublicKey object
    :cvar SECRET_SEED: cryp::SecretSeed object
    :cvar SIGNATURE: cryp::Signature object (asymmetric digital
        signature or symmetric MAC/HMAC)
    :cvar SYMMETRIC_KEY: cryp::SymmetricKey object
    :cvar UNDEFINED: Object type unknown
    """

    PRIVATE_KEY = "PRIVATE-KEY"
    PUBLIC_KEY = "PUBLIC-KEY"
    SECRET_SEED = "SECRET-SEED"
    SIGNATURE = "SIGNATURE"
    SYMMETRIC_KEY = "SYMMETRIC-KEY"
    UNDEFINED = "UNDEFINED"
