from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_profile_type_3 import TypeProfileType3

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeProfileParentHistory1:
    """
    Parameters
    ----------
    profile_id
        Agency in which the field group is created.
    profile_type
        The type of profile this profile is for (e.g., branch, account,
        traveler). The profile type identifies which default
        attributes/elements (minimum data set) the system will insert.
    profile_name
        The name of the profile. Either the concatenated first name or last
        name of a Agent or Traveler or the name of the other profile.
    provisioning_code
        The Provisioning Code for this profile.
    """

    class Meta:
        name = "typeProfileParentHistory"

    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
        },
    )
    profile_type: None | TypeProfileType3 = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
        },
    )
    profile_name: None | str = field(
        default=None,
        metadata={
            "name": "ProfileName",
            "type": "Attribute",
        },
    )
    provisioning_code: None | str = field(
        default=None,
        metadata={
            "name": "ProvisioningCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 25,
        },
    )
