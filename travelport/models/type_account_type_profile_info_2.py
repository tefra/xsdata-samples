from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_profile_info_2 import TypeProfileInfo2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class TypeAccountTypeProfileInfo2(TypeProfileInfo2):
    """
    History Element for Traveler Group.

    Parameters
    ----------
    mid_office_id
        Mid Office identifier managed by an external system.
    """

    class Meta:
        name = "typeAccountTypeProfileInfo"

    mid_office_id: None | str = field(
        default=None,
        metadata={
            "name": "MidOfficeID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
