from dataclasses import dataclass, field
from typing import Optional

from .crypto_certificate_algorithm_family_enum_simple import (
    CryptoCertificateAlgorithmFamilyEnumSimple,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CryptoCertificateAlgorithmFamilyEnum:
    """
    This meta-class defies possible cryptographic algorithm families used to create
    public keys and  signatures within the certificate.

    :ivar value:
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    """

    class Meta:
        name = "CRYPTO-CERTIFICATE-ALGORITHM-FAMILY-ENUM"

    value: Optional[CryptoCertificateAlgorithmFamilyEnumSimple] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
