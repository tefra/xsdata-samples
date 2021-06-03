from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CryptoCertificateFormatEnumSimple(Enum):
    """
    :cvar CVC: The certificate has been created in Card Verifiable
        Certificate (CVC) format
    :cvar X_509: The certificate is created in X.509 format.
    """
    CVC = "CVC"
    X_509 = "X-509"
