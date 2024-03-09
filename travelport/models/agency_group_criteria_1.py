from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_profile_search_criteria_1 import (
    TypeProfileSearchCriteria1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class AgencyGroupCriteria1(TypeProfileSearchCriteria1):
    """
    Agency Group search modifiers.

    Parameters
    ----------
    name
        Agency Group name wild card
    """

    class Meta:
        name = "AgencyGroupCriteria"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )
