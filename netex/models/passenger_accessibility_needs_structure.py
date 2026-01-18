from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .suitability import Suitability
from .user_need import UserNeed

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerAccessibilityNeedsStructure:
    accompanied_by_carer: bool | None = field(
        default=None,
        metadata={
            "name": "AccompaniedByCarer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    user_needs: PassengerAccessibilityNeedsStructure.UserNeeds | None = field(
        default=None,
        metadata={
            "name": "userNeeds",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    suitabilities: (
        PassengerAccessibilityNeedsStructure.Suitabilities | None
    ) = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass
    class UserNeeds:
        user_need: Iterable[UserNeed] = field(
            default_factory=list,
            metadata={
                "name": "UserNeed",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )

    @dataclass
    class Suitabilities:
        suitability: Iterable[Suitability] = field(
            default_factory=list,
            metadata={
                "name": "Suitability",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
