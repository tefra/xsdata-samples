from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_profile_search_criteria_2 import TypeProfileSearchCriteria2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class AgencyGroupCriteria2(TypeProfileSearchCriteria2):
    """
    Agency Group search modifiers.

    Parameters
    ----------
    name
        Agency Group name wild card
    """
    class Meta:
        name = "AgencyGroupCriteria"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        }
    )
