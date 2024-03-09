from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_profile_info_1 import TypeProfileInfo1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeAgencyGroupInfoHistory1(TypeProfileInfo1):
    """
    History Element for AgencyGroupInfo.

    Parameters
    ----------
    name
        Name of Agency Group
    """

    class Meta:
        name = "typeAgencyGroupInfoHistory"

    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
