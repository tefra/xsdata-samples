from __future__ import annotations

from dataclasses import dataclass, field

from .persistency_redundancy_handling_scope_enum import (
    PersistencyRedundancyHandlingScopeEnum,
)
from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class PersistencyRedundancyMOutOfN:
    """
    This meta-class provides the ability to describe redundancy via an "M
    out of N" approach.

    In this case N is the number of copies created and M is the minimum
    number of identical copies to justify a reliable read access to the
    data.

    :ivar scope: This attribute controls the scope in which the
        redundancy handling is applied.
    :ivar m: This attribute represents the "M" coordinate in the "M out
        of N" scheme.
    :ivar n: This attribute represents the "N" coordinate in the "M out
        of N" scheme.
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
        name = "PERSISTENCY-REDUNDANCY-M-OUT-OF-N"

    scope: None | PersistencyRedundancyHandlingScopeEnum = field(
        default=None,
        metadata={
            "name": "SCOPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    m: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "M",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    n: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "N",
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
