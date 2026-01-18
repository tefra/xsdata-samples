from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_account_type_profile_info_2 import (
    TypeAccountTypeProfileInfo2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class TypeTravelerGroupInfoHistory2(TypeAccountTypeProfileInfo2):
    """
    History Element for Traveler Group.

    Parameters
    ----------
    name
        Name of the TravelerGroup
    local_language_name
        The name of the TravelerGroup in the user's local language.
    """

    class Meta:
        name = "typeTravelerGroupInfoHistory"

    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    local_language_name: None | str = field(
        default=None,
        metadata={
            "name": "LocalLanguageName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
