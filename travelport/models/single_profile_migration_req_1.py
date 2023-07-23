from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_2 import BaseReq2
from travelport.models.type_profile_type_2 import TypeProfileType2

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class SingleProfileMigrationReq1(BaseReq2):
    """
    Request to initiate the migration process of a single Account or Traveler
    profile from host to uProfile.

    Parameters
    ----------
    external_system
        ExternalSystem to indicate the origin  system of profile. Currently
        supported for 1G,1V. Future enhancement may include TDS, CSV, 1P.
    profile_type
        The type of the Profile to be migrated.e.g- Account , Traveler
    pcc
        The PCC of the Profile to be migrated.
    account_profile_title
        Account Profile Title which need to be migrated.
    traveler_profile_title
        Traveler Profile Title which need to be migrated.
    """
    class Meta:
        name = "SingleProfileMigrationReq"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    external_system: None | str = field(
        default=None,
        metadata={
            "name": "ExternalSystem",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 10,
        }
    )
    profile_type: None | TypeProfileType2 = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
    pcc: None | str = field(
        default=None,
        metadata={
            "name": "PCC",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 10,
        }
    )
    account_profile_title: None | str = field(
        default=None,
        metadata={
            "name": "AccountProfileTitle",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 50,
        }
    )
    traveler_profile_title: None | str = field(
        default=None,
        metadata={
            "name": "TravelerProfileTitle",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 50,
        }
    )
