from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .suitability import Suitability
from .user_need import UserNeed

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerAccessibilityNeedsStructure:
    accompanied_by_carer: None | bool = field(
        default=None,
        metadata={
            "name": "AccompaniedByCarer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    user_needs: None | PassengerAccessibilityNeedsStructure.UserNeeds = field(
        default=None,
        metadata={
            "name": "userNeeds",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    suitabilities: (
        None | PassengerAccessibilityNeedsStructure.Suitabilities
    ) = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass(kw_only=True)
    class UserNeeds:
        user_need: Sequence[UserNeed] = field(
            default_factory=list,
            metadata={
                "name": "UserNeed",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )

    @dataclass(kw_only=True)
    class Suitabilities:
        suitability: Sequence[Suitability] = field(
            default_factory=list,
            metadata={
                "name": "Suitability",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
