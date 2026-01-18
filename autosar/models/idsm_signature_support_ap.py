from __future__ import annotations

from dataclasses import dataclass, field

from .crypto_key_slot_subtypes_enum import CryptoKeySlotSubtypesEnum
from .ref import Ref
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class IdsmSignatureSupportAp:
    """
    This meta-class defines, for the Adaptive Platform, the cryptographic
    algorithm and key to be used by the IdsM instance for providing
    signature information in QSEv messages.

    :ivar crypto_primitive: This attribute defines the cryptographic
        algorithm to be used for providing authentication information in
        QSEv messages. The content of this attribute shall comply to the
        "Cryptographic Primitives Naming Convention".
    :ivar key_slot_ref: This reference denotes the cryptographic key to
        be used by the cryptographic algorithm for providing
        authentication information in QSEv messages.
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
        name = "IDSM-SIGNATURE-SUPPORT-AP"

    crypto_primitive: None | String = field(
        default=None,
        metadata={
            "name": "CRYPTO-PRIMITIVE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    key_slot_ref: None | IdsmSignatureSupportAp.KeySlotRef = field(
        default=None,
        metadata={
            "name": "KEY-SLOT-REF",
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
    class KeySlotRef(Ref):
        dest: CryptoKeySlotSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
