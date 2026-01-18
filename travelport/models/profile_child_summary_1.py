from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_profile_entity_status_1 import (
    TypeProfileEntityStatus1,
)
from travelport.models.type_profile_type_3 import TypeProfileType3

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class ProfileChildSummary1:
    """
    Parameters
    ----------
    profile_id
        The system-assigned, unique ID of the profile.
    profile_type
        The type of profile this profile is for (e.g., branch, account,
        traveler). The profile type identifies which default
        attributes/elements (minimum data set) the system will insert.
    name
        The Name of the profile. For profiles of type Agent, concatenate the
        GivenName and Surname values from the agent table, and return as a
        single attribute in the response.
    provisioning_code
        The provisioning ID/code of the profile, if applicable.
    status
        Profile status (Active, Inactive, Pending, Disabled).
    version
        Version of the profile.
    control
        Identify if the entity is a control branch or not.
    description
    """

    class Meta:
        name = "ProfileChildSummary"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_id: int = field(
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_type: TypeProfileType3 = field(
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    provisioning_code: None | str = field(
        default=None,
        metadata={
            "name": "ProvisioningCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    status: TypeProfileEntityStatus1 = field(
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
    version: int = field(
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        }
    )
    control: bool = field(
        default=False,
        metadata={
            "name": "Control",
            "type": "Attribute",
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
