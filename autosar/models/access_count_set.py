from dataclasses import dataclass, field
from typing import Optional

from .access_count import AccessCount
from .admin_data import VariationPoint
from .nmtoken_string import NmtokenString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class AccessCountSet:
    """
    This meta-class provides a set of count values evaluated according to
    the rules of a specific countProfile.

    :ivar access_counts: Count value for a AbstractAccessPoint. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar count_profile: This attribute defines the name of the count
        profile used to determine the AccessCount.value numbers.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "ACCESS-COUNT-SET"

    access_counts: Optional["AccessCountSet.AccessCounts"] = field(
        default=None,
        metadata={
            "name": "ACCESS-COUNTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    count_profile: Optional[NmtokenString] = field(
        default=None,
        metadata={
            "name": "COUNT-PROFILE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
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

    @dataclass
    class AccessCounts:
        access_count: list[AccessCount] = field(
            default_factory=list,
            metadata={
                "name": "ACCESS-COUNT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
