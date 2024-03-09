from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.applied_profile_criteria import AppliedProfileCriteria
from travelport.models.name_criteria import NameCriteria

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class TravelerCriteria1:
    """
    Criteria for Searching misc traveler information.

    Parameters
    ----------
    name_criteria
    applied_profile_criteria
    phone_number
        To Search for Phone Number match
    viponly
        To Search for VIP traveler
    """

    class Meta:
        name = "TravelerCriteria"
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    name_criteria: None | NameCriteria = field(
        default=None,
        metadata={
            "name": "NameCriteria",
            "type": "Element",
        },
    )
    applied_profile_criteria: None | AppliedProfileCriteria = field(
        default=None,
        metadata={
            "name": "AppliedProfileCriteria",
            "type": "Element",
        },
    )
    phone_number: None | str = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Attribute",
        },
    )
    viponly: None | bool = field(
        default=None,
        metadata={
            "name": "VIPOnly",
            "type": "Attribute",
        },
    )
