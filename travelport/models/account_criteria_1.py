from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_account_type_profile_search_criteria_1 import (
    TypeAccountTypeProfileSearchCriteria1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class AccountCriteria1(TypeAccountTypeProfileSearchCriteria1):
    """
    Account search modifiers.

    Parameters
    ----------
    name
        Account name wild card
    """

    class Meta:
        name = "AccountCriteria"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )
