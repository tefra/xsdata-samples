from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .crypto_service_key_subtypes_enum import CryptoServiceKeySubtypesEnum
from .ref import Ref
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TlsPskIdentity:
    """
    This element is used to describe the pre-shared key shared during the
    handshake among the communication parties, to establish a TLS
    connection if the handshake is based on the existence of a pre-shared
    key.

    :ivar pre_shared_key_ref: This reference identifies the applicable
        cryptograhic key.
    :ivar psk_identity: This attribute provides the key identification.
    :ivar psk_identity_hint: This attribute provides the identity hint
        for a pre-shared key.
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
        name = "TLS-PSK-IDENTITY"

    pre_shared_key_ref: TlsPskIdentity.PreSharedKeyRef | None = field(
        default=None,
        metadata={
            "name": "PRE-SHARED-KEY-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    psk_identity: String | None = field(
        default=None,
        metadata={
            "name": "PSK-IDENTITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    psk_identity_hint: String | None = field(
        default=None,
        metadata={
            "name": "PSK-IDENTITY-HINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class PreSharedKeyRef(Ref):
        dest: CryptoServiceKeySubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
