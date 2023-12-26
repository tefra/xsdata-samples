from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CryptoCertificateAlgorithmFamilyEnumSimple(Enum):
    """
    :cvar ECC: The cryptographic operations in the certificate are
        executed using elliptic curves (ecc)
    :cvar RSA: The cryptographic operations in the certificate are
        executed using the RSA approach.
    """

    ECC = "ECC"
    RSA = "RSA"
