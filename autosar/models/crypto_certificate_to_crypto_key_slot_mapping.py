from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.crypto_certificate_subtypes_enum import CryptoCertificateSubtypesEnum
from autosar.models.crypto_key_slot_subtypes_enum import CryptoKeySlotSubtypesEnum
from autosar.models.ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CryptoCertificateToCryptoKeySlotMapping:
    """
    This meta-class represents the ability to define a mapping between a
    CryptoKeySlot and a CryptoCertificate.

    :ivar crypto_certificate_ref: This reference represents the mapped
        cryptoCertificate.
    :ivar crypto_key_slot_refs: This reference represents the mapped
        cryptoKeySlot.
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
        name = "CRYPTO-CERTIFICATE-TO-CRYPTO-KEY-SLOT-MAPPING"

    crypto_certificate_ref: Optional["CryptoCertificateToCryptoKeySlotMapping.CryptoCertificateRef"] = field(
        default=None,
        metadata={
            "name": "CRYPTO-CERTIFICATE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    crypto_key_slot_refs: Optional["CryptoCertificateToCryptoKeySlotMapping.CryptoKeySlotRefs"] = field(
        default=None,
        metadata={
            "name": "CRYPTO-KEY-SLOT-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )

    @dataclass
    class CryptoCertificateRef(Ref):
        dest: Optional[CryptoCertificateSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class CryptoKeySlotRefs:
        crypto_key_slot_ref: List["CryptoCertificateToCryptoKeySlotMapping.CryptoKeySlotRefs.CryptoKeySlotRef"] = field(
            default_factory=list,
            metadata={
                "name": "CRYPTO-KEY-SLOT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
                "max_occurs": 2,
            }
        )

        @dataclass
        class CryptoKeySlotRef(Ref):
            dest: Optional[CryptoKeySlotSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )
