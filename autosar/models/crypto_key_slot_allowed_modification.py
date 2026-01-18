from __future__ import annotations

from dataclasses import dataclass, field

from .boolean import Boolean
from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class CryptoKeySlotAllowedModification:
    """
    This meta-class restricts the allowed modification of a key stored in
    the key slot.

    :ivar allow_content_type_change: This attribute describes whether
        the key content type can be changed (true) or not (false), e.g.
        changing the key from symmetric to RSA.
    :ivar exportability: This attribute describes whether the key slot
        content is allowed to be exported or not.
    :ivar max_number_of_allowed_updates: This attribute describes the
        maximum updates that are allowed to the slot.
    :ivar restrict_update: This attribute defines whether restrictions
        on the number of updates are defined or not. False: no
        restriction is placed on the number of updates. True:
        restrictions are placed on the number of updates with the
        attribute maxNumberOfAllowedUpdates.
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
        name = "CRYPTO-KEY-SLOT-ALLOWED-MODIFICATION"

    allow_content_type_change: None | Boolean = field(
        default=None,
        metadata={
            "name": "ALLOW-CONTENT-TYPE-CHANGE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    exportability: None | Boolean = field(
        default=None,
        metadata={
            "name": "EXPORTABILITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_number_of_allowed_updates: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "MAX-NUMBER-OF-ALLOWED-UPDATES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    restrict_update: None | Boolean = field(
        default=None,
        metadata={
            "name": "RESTRICT-UPDATE",
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
