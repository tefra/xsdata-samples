from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_5 import BaseReq5
from travelport.models.profile_modify_cmd_2 import ProfileModifyCmd2
from travelport.models.provisioning_code_profile_type_12 import (
    ProvisioningCodeProfileType12,
)
from travelport.models.unique_profile_id_profile_type_12 import (
    UniqueProfileIdProfileType12,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileModifyReq2(BaseReq5):
    """Request to add, change, or remove data on a specific profile.

    Either ProfileID or ProvisioningCode are mandatory.

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
    profile_modify_cmd
    version
        Version number of the profile. Required with every modify request.
    return_profile
        If false will only return basic Profile information, without the
        updated profile data. If true, will return the entire profile and
        all its data (including data not modified by this transaction).
    show_data_unmasked
        Set to true to show in the response all data in the requested
        profile, without masking applied. (Any such data in parent profiles
        will still be masked.) Requires special authorization.
    """

    class Meta:
        name = "ProfileModifyReq"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Element",
        },
    )
    provisioning_code: None | ProfileModifyReq2.ProvisioningCode = field(
        default=None,
        metadata={
            "name": "ProvisioningCode",
            "type": "Element",
        },
    )
    unique_profile_id: None | ProfileModifyReq2.UniqueProfileId = field(
        default=None,
        metadata={
            "name": "UniqueProfileID",
            "type": "Element",
        },
    )
    profile_modify_cmd: list[ProfileModifyCmd2] = field(
        default_factory=list,
        metadata={
            "name": "ProfileModifyCmd",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    version: None | int = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        },
    )
    return_profile: bool = field(
        default=False,
        metadata={
            "name": "ReturnProfile",
            "type": "Attribute",
        },
    )
    show_data_unmasked: bool = field(
        default=False,
        metadata={
            "name": "ShowDataUnmasked",
            "type": "Attribute",
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
        profile_type: None | ProvisioningCodeProfileType12 = field(
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
        profile_type: None | UniqueProfileIdProfileType12 = field(
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
