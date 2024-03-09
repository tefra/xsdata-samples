from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_account_type_profile_search_criteria_2 import (
    TypeAccountTypeProfileSearchCriteria2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TravelerGroupCriteria2(TypeAccountTypeProfileSearchCriteria2):
    """
    Traveler Group search modifiers.

    Parameters
    ----------
    name
        Traveler Group name wild card
    """

    class Meta:
        name = "TravelerGroupCriteria"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )
