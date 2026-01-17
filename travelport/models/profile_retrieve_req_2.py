from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_5 import BaseReq5
from travelport.models.profile_data_filter_2 import ProfileDataFilter2
from travelport.models.provisioning_code_profile_type_2 import (
    ProvisioningCodeProfileType2,
)
from travelport.models.unique_profile_id_profile_type_2 import (
    UniqueProfileIdProfileType2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileRetrieveReq2(BaseReq5):
    """
    Request to retrieve a particular profile.

    Either the full parent profiles or a summary can also be requested on
    the response. Either ProfileID or ProvisioningCode are mandatory.

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
    profile_data_filter
    return_parent
        If true, the response will include profile information from this
        profile's parents. only inheritable data will be returned.
    return_parent_summary
        If true, the response will include profile summary information from
        this profile's parents.
    show_data_unmasked
        Set to true to show in the response all data in the requested
        profile, without masking applied. (Any such data in parent profiles
        will still be masked.) Requires special authorization.
    full_parent_hierarchy
        Set to false to show in the response only the data upto and
        including Account, for Traveler and TravelerGroup.For Account just
        it's own Profile will be returned.
    parent_id
        For traveler profile retrieve, the specific immediate parent from
        which to return inherited data when ReturnParent is true. Ignored
        otherwise.
    """

    class Meta:
        name = "ProfileRetrieveReq"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Element",
        },
    )
    provisioning_code: None | ProfileRetrieveReq2.ProvisioningCode = field(
        default=None,
        metadata={
            "name": "ProvisioningCode",
            "type": "Element",
        },
    )
    unique_profile_id: None | ProfileRetrieveReq2.UniqueProfileId = field(
        default=None,
        metadata={
            "name": "UniqueProfileID",
            "type": "Element",
        },
    )
    profile_data_filter: None | ProfileDataFilter2 = field(
        default=None,
        metadata={
            "name": "ProfileDataFilter",
            "type": "Element",
        },
    )
    return_parent: None | bool = field(
        default=None,
        metadata={
            "name": "ReturnParent",
            "type": "Attribute",
        },
    )
    return_parent_summary: None | bool = field(
        default=None,
        metadata={
            "name": "ReturnParentSummary",
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
    full_parent_hierarchy: bool = field(
        default=True,
        metadata={
            "name": "FullParentHierarchy",
            "type": "Attribute",
        },
    )
    parent_id: None | int = field(
        default=None,
        metadata={
            "name": "ParentID",
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
