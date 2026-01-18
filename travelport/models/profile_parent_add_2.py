from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.provisioning_code_profile_type_2 import (
    ProvisioningCodeProfileType2,
)
from travelport.models.unique_profile_id_profile_type_2 import (
    UniqueProfileIdProfileType2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class ProfileParentAdd2:
    """
    Command to add a new parent profile.

    Parameters
    ----------
    profile_id
        Specify the Profile ID
    provisioning_code
        Specify the Provisioning Code with the profile Type
    unique_profile_id
        Applicable to retrieve, modify and delete a traveler profile.
        Combination of UniqueProfileID and AgencyCode can be used in place
        of Profile ID. Cannot be used with ProfileParentAdd,
        ProfileParentDelete or ProfileChildSearch.
    """

    class Meta:
        name = "ProfileParentAdd"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Element",
        },
    )
    provisioning_code: None | ProfileParentAdd2.ProvisioningCode = field(
        default=None,
        metadata={
            "name": "ProvisioningCode",
            "type": "Element",
        },
    )
    unique_profile_id: None | ProfileParentAdd2.UniqueProfileId = field(
        default=None,
        metadata={
            "name": "UniqueProfileID",
            "type": "Element",
        },
    )

    @dataclass(kw_only=True)
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
        profile_type: ProvisioningCodeProfileType2 = field(
            metadata={
                "name": "ProfileType",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
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
        profile_type: UniqueProfileIdProfileType2 = field(
            metadata={
                "name": "ProfileType",
                "type": "Attribute",
                "required": True,
            }
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
