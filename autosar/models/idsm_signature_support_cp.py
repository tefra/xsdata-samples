from __future__ import annotations

from dataclasses import dataclass, field

from .crypto_service_key_subtypes_enum import CryptoServiceKeySubtypesEnum
from .crypto_service_primitive_subtypes_enum import (
    CryptoServicePrimitiveSubtypesEnum,
)
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class IdsmSignatureSupportCp:
    """
    This meta-class defines, for the Classic Platform, the cryptographic
    algorithm and key to be used by the IdsM instance for providing
    signature information in QSEv messages.

    :ivar authentication_ref: This reference dennotes the cryptographic
        primitives for providing authentication information in QSEv
        messages.
    :ivar crypto_service_key_ref: This reference denotes the
        cryptographic key to be used by the cryptographic algorithm for
        providing authentication information in QSEv messages.
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
        name = "IDSM-SIGNATURE-SUPPORT-CP"

    authentication_ref: None | IdsmSignatureSupportCp.AuthenticationRef = (
        field(
            default=None,
            metadata={
                "name": "AUTHENTICATION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    crypto_service_key_ref: (
        None | IdsmSignatureSupportCp.CryptoServiceKeyRef
    ) = field(
        default=None,
        metadata={
            "name": "CRYPTO-SERVICE-KEY-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass(kw_only=True)
    class AuthenticationRef(Ref):
        dest: CryptoServicePrimitiveSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class CryptoServiceKeyRef(Ref):
        dest: CryptoServiceKeySubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
