from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_profile_search_criteria_1 import (
    TypeProfileSearchCriteria1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class AgencyCriteria1(TypeProfileSearchCriteria1):
    """
    Agency search modifiers.

    Parameters
    ----------
    name
        Agency name wild card
    agency_code
        Zircon site ID
    iata_number
        IATA Number wild card
    """

    class Meta:
        name = "AgencyCriteria"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )
    agency_code: None | str = field(
        default=None,
        metadata={
            "name": "AgencyCode",
            "type": "Attribute",
        },
    )
    iata_number: None | str = field(
        default=None,
        metadata={
            "name": "IataNumber",
            "type": "Attribute",
        },
    )
