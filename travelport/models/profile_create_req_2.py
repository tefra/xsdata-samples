from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_5 import BaseReq5
from travelport.models.profile_data_2 import ProfileData2
from travelport.models.profile_link_2 import ProfileLink2
from travelport.models.provisioning_code_profile_type_2 import (
    ProvisioningCodeProfileType2,
)
from travelport.models.type_profile_entity_status_2 import (
    TypeProfileEntityStatus2,
)
from travelport.models.type_profile_type_7 import TypeProfileType7
from travelport.models.unique_profile_id_profile_type_2 import (
    UniqueProfileIdProfileType2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileCreateReq2(BaseReq5):
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
    template_id
        The unique ID of the profile template associated to this entity.
        Cannot be modified after the profile is created.
    template_version
        The current version number of the template.
    hierarchy_level_id
        System-defined, unique identifier of the level in the profile's
        hierarchy to which this profile is associated.
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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_parent: None | ProfileCreateReq2.ProfileParent = field(
        default=None,
        metadata={
            "name": "ProfileParent",
            "type": "Element",
        },
    )
    profile_data: None | ProfileData2 = field(
        default=None,
        metadata={
            "name": "ProfileData",
            "type": "Element",
            "required": True,
        },
    )
    profile_link: list[ProfileLink2] = field(
        default_factory=list,
        metadata={
            "name": "ProfileLink",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    profile_type: None | TypeProfileType7 = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        },
    )
    status: TypeProfileEntityStatus2 = field(
        default=TypeProfileEntityStatus2.ACTIVE,
        metadata={
            "name": "Status",
            "type": "Attribute",
        },
    )
    template_id: None | int = field(
        default=None,
        metadata={
            "name": "TemplateID",
            "type": "Attribute",
        },
    )
    template_version: None | int = field(
        default=None,
        metadata={
            "name": "TemplateVersion",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
    hierarchy_level_id: None | str = field(
        default=None,
        metadata={
            "name": "HierarchyLevelID",
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
            Applicable to retrieve, modify and delete a traveler profile.
            Combination of UniqueProfileID and AgencyCode can be used in
            place of Profile ID. Cannot be used with ProfileParentAdd,
            ProfileParentDelete or ProfileChildSearch.
        """

        profile_id: None | int = field(
            default=None,
            metadata={
                "name": "ProfileID",
                "type": "Element",
            },
        )
        provisioning_code: (
            None | ProfileCreateReq2.ProfileParent.ProvisioningCode
        ) = field(
            default=None,
            metadata={
                "name": "ProvisioningCode",
                "type": "Element",
            },
        )
        unique_profile_id: (
            None | ProfileCreateReq2.ProfileParent.UniqueProfileId
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
