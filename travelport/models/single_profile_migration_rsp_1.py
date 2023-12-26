from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_2 import BaseRsp2
from travelport.models.type_profile_type_2 import TypeProfileType2

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class SingleProfileMigrationRsp1(BaseRsp2):
    """
    Response of migration process of a single Account or Traveler profile from host
    to uProfile.

    Parameters
    ----------
    profile_id
        The system-assigned, unique ID of the profile.
    status
        Status of the migration process.
    profile_type
        The type of the migrated Profile e.g-Account,Traveler
    """

    class Meta:
        name = "SingleProfileMigrationRsp"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
        },
    )
    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    profile_type: None | TypeProfileType2 = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
        },
    )
