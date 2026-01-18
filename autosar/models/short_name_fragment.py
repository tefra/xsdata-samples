from __future__ import annotations

from dataclasses import dataclass, field

from .identifier import Identifier
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class ShortNameFragment:
    """
    This class describes how the Referrable.shortName is composed of
    several shortNameFragments.

    :ivar role: This specifies the role of fragment to define e.g. the
        order of the fragments.
    :ivar fragment: This specifies a single shortName (fragment) which
        is part of the composed shortName.
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
        name = "SHORT-NAME-FRAGMENT"

    role: None | String = field(
        default=None,
        metadata={
            "name": "ROLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    fragment: None | Identifier = field(
        default=None,
        metadata={
            "name": "FRAGMENT",
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
