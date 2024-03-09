from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_2 import BaseReq2
from travelport.models.profile_data_1 import ProfileData1
from travelport.models.profile_link_1 import ProfileLink1
from travelport.models.provisioning_code_profile_type_1 import (
    ProvisioningCodeProfileType1,
)
from travelport.models.type_profile_entity_status_1 import (
    TypeProfileEntityStatus1,
)
from travelport.models.type_profile_type_3 import TypeProfileType3
from travelport.models.unique_profile_id_profile_type_1 import (
    UniqueProfileIdProfileType1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileCreateReq1(BaseReq2):
    """
    Creates a new profile.

    Parameters
    ----------
    profile_parent
        Most profiles will have a single parent.AgencyGroup Profiles will
        have no parents and Agency profile may not have a parent.  This data
        is not returned in the response.
    profile_data
        Profile data.
    profile_link
        A unidirectional link from one profile to another.
    profile_type
        The type of the Profile to be created.
    status
        Status of the profile entity (e.g., Active, Inactive). Any status
        other than Active implies that the entity cannot perform most
        transactions.
    return_profile
        If true, will return basic information with the ProfileData element
        and its associated data.
    show_data_unmasked
        Set to true to show in the response all data in the requested
        profile, without masking applied. (Any such data in parent profiles
        will still be masked.) Requires special authorization.
    """

    class Meta:
        name = "ProfileCreateReq"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_parent: None | ProfileCreateReq1.ProfileParent = field(
        default=None,
        metadata={
            "name": "ProfileParent",
            "type": "Element",
        },
    )
    profile_data: None | ProfileData1 = field(
        default=None,
        metadata={
            "name": "ProfileData",
            "type": "Element",
            "required": True,
        },
    )
    profile_link: list[ProfileLink1] = field(
        default_factory=list,
        metadata={
            "name": "ProfileLink",
            "type": "Element",
        },
    )
    profile_type: None | TypeProfileType3 = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        },
    )
    status: TypeProfileEntityStatus1 = field(
        default=TypeProfileEntityStatus1.ACTIVE,
        metadata={
            "name": "Status",
            "type": "Attribute",
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
    class ProfileParent:
        """
        Parameters
        ----------
        profile_id
            Specify the Profile ID
        provisioning_code
            Specify the Provisioning Code with the profile Type
        unique_profile_id
            Applicable to retrieve ,modify and delete a traveler profile.
            Can be used in place of the ProfileID. Cannot be used with
            ProfileParentAdd, ProfileParentDelete or ProfileChildSearch.
        """

        profile_id: None | int = field(
            default=None,
            metadata={
                "name": "ProfileID",
                "type": "Element",
            },
        )
        provisioning_code: (
            None | ProfileCreateReq1.ProfileParent.ProvisioningCode
        ) = field(
            default=None,
            metadata={
                "name": "ProvisioningCode",
                "type": "Element",
            },
        )
        unique_profile_id: (
            None | ProfileCreateReq1.ProfileParent.UniqueProfileId
        ) = field(
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
            profile_type: None | ProvisioningCodeProfileType1 = field(
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
                Specify the Profile Type (limited to only the ones where
                Profile Identifier is relevant)
            agency_code
                'AgencyCode' is the Provisioning code of the parent Agency.
                This is an optional attribute and if not provided, the
                system will determine 'AgencyCode' by Agent's WAB/target
                Branch or Agent's agency.
            """

            value: str = field(
                default="",
                metadata={
                    "required": True,
                    "min_length": 6,
                    "max_length": 128,
                },
            )
            profile_type: None | UniqueProfileIdProfileType1 = field(
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
