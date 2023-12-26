from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_5 import BaseReq5
from travelport.models.provisioning_code_profile_type_2 import (
    ProvisioningCodeProfileType2,
)
from travelport.models.unique_profile_id_profile_type_2 import (
    UniqueProfileIdProfileType2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileDeleteReq2(BaseReq5):
    """Request to delete a particular profile.

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
    force
        To specify that this is a Force Delete.  With a Force Delete, the
        profile specified and any children below that profile will be
        deleted.
    """

    class Meta:
        name = "ProfileDeleteReq"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Element",
        },
    )
    provisioning_code: None | ProfileDeleteReq2.ProvisioningCode = field(
        default=None,
        metadata={
            "name": "ProvisioningCode",
            "type": "Element",
        },
    )
    unique_profile_id: None | ProfileDeleteReq2.UniqueProfileId = field(
        default=None,
        metadata={
            "name": "UniqueProfileID",
            "type": "Element",
        },
    )
    force: bool = field(
        default=False,
        metadata={
            "name": "Force",
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
