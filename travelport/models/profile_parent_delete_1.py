from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.provisioning_code_profile_type_2 import (
    ProvisioningCodeProfileType2,
)
from travelport.models.unique_profile_id_profile_type_2 import (
    UniqueProfileIdProfileType2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileParentDelete1:
    """
    Command to delete a parent profile.

    Parameters
    ----------
    profile_id
        Specify the Profile ID
    provisioning_code
        Specify the Provisioning Code with the profile Type
    unique_profile_id
        Applicable to retrieve ,modify and delete a traveler profile. Can be
        used in place of the ProfileID. Cannot be used with
        ProfileParentAdd, ProfileParentDelete or ProfileChildSearch.
    """

    class Meta:
        name = "ProfileParentDelete"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Element",
        },
    )
    provisioning_code: None | ProfileParentDelete1.ProvisioningCode = field(
        default=None,
        metadata={
            "name": "ProvisioningCode",
            "type": "Element",
        },
    )
    unique_profile_id: None | ProfileParentDelete1.UniqueProfileId = field(
        default=None,
        metadata={
            "name": "UniqueProfileID",
            "type": "Element",
        },
    )

    @dataclass
    class ProvisioningCode:
        """
        Parameters
        ----------
        value
        profile_type
            Specify the Profile Type (limited to only the ones where
            ProvisioningCode is relevant)
        """

        value: str = field(
            default="",
            metadata={
                "required": True,
                "min_length": 1,
                "max_length": 128,
            },
        )
        profile_type: None | ProvisioningCodeProfileType2 = field(
            default=None,
            metadata={
                "name": "ProfileType",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class UniqueProfileId:
        """
        Parameters
        ----------
        value
        profile_type
            Specify the Profile Type (limited to only the ones where Profile
            Identifier is relevant)
        agency_code
            'AgencyCode' is the Provisioning code of the parent Agency. This
            is an optional attribute and if not provided, the system will
            determine 'AgencyCode' by Agent's WAB/target Branch or Agent's
            agency.
        """

        value: str = field(
            default="",
            metadata={
                "required": True,
                "min_length": 6,
                "max_length": 128,
            },
        )
        profile_type: None | UniqueProfileIdProfileType2 = field(
            default=None,
            metadata={
                "name": "ProfileType",
                "type": "Attribute",
                "required": True,
            },
        )
        agency_code: None | str = field(
            default=None,
            metadata={
                "name": "AgencyCode",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 25,
            },
        )
