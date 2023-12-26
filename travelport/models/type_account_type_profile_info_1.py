from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_profile_info_1 import TypeProfileInfo1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeAccountTypeProfileInfo1(TypeProfileInfo1):
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
