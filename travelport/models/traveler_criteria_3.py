from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_account_type_profile_search_criteria_2 import (
    TypeAccountTypeProfileSearchCriteria2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TravelerCriteria3(TypeAccountTypeProfileSearchCriteria2):
    """
    Traveler search modifiers.

    Parameters
    ----------
    given_name
        Given name wild card
    surname
        Surname wild card
    """

    class Meta:
        name = "TravelerCriteria"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    given_name: None | str = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Attribute",
        },
    )
    surname: None | str = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Attribute",
        },
    )
