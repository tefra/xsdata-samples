from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_profile_info_2 import TypeProfileInfo2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class TypeAgencyGroupInfoHistory2(TypeProfileInfo2):
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
