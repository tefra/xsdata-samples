from dataclasses import dataclass, field
from typing import List, Optional

from .suitability import Suitability
from .user_need import UserNeed

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerAccessibilityNeedsStructure:
    accompanied_by_carer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AccompaniedByCarer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    user_needs: Optional["PassengerAccessibilityNeedsStructure.UserNeeds"] = (
        field(
            default=None,
            metadata={
                "name": "userNeeds",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    suitabilities: Optional[
        "PassengerAccessibilityNeedsStructure.Suitabilities"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass
    class UserNeeds:
        user_need: List[UserNeed] = field(
            default_factory=list,
            metadata={
                "name": "UserNeed",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )

    @dataclass
    class Suitabilities:
        suitability: List[Suitability] = field(
            default_factory=list,
            metadata={
                "name": "Suitability",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
