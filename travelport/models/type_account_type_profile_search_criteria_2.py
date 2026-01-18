from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_profile_search_criteria_2 import (
    TypeProfileSearchCriteria2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class TypeAccountTypeProfileSearchCriteria2(TypeProfileSearchCriteria2):
    """
    Search criteria for Accounts, Traveler Groups and Travellers.

    Parameters
    ----------
    mid_office_id
        Mid Office ID managed by an external system.
    """

    class Meta:
        name = "typeAccountTypeProfileSearchCriteria"

    mid_office_id: None | str = field(
        default=None,
        metadata={
            "name": "MidOfficeID",
            "type": "Attribute",
        },
    )
