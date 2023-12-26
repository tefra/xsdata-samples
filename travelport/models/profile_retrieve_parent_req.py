from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_2 import BaseReq2
from travelport.models.profile_data_filter_1 import ProfileDataFilter1
from travelport.models.provisioning_code_profile_type_1 import (
    ProvisioningCodeProfileType1,
)
from travelport.models.type_parent_profile_level import TypeParentProfileLevel
from travelport.models.unique_profile_id_profile_type_1 import (
    UniqueProfileIdProfileType1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileRetrieveParentReq(BaseReq2):
    """
    Service to retrieve parent data.

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
    profile_data_filter
    parent_profile_id
        Unique ID of the Parent profile for which the data will be returned.
    parent_summary
        If specified ‘true’ then it just returns the summary information of
        profile's parents.  If it is false, then it returns the entire
        hierarchy.
    show_data_unmasked
        Set to true to show in the response all data in the requested
        profile, without masking applied. (Any such data in parent profiles
        will still be masked.) Requires special authorization.
    parent_level_to_return
        Returns parent’s data up to specified hierarchy. Valid values are
        ‘Agency’, ‘AgencyGroup’, ‘BranchGroup’, ‘Branch’, ‘Account’ and
        ‘Traveler Group’.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Element",
        },
    )
    provisioning_code: None | ProfileRetrieveParentReq.ProvisioningCode = (
        field(
            default=None,
            metadata={
                "name": "ProvisioningCode",
                "type": "Element",
            },
        )
    )
    unique_profile_id: None | ProfileRetrieveParentReq.UniqueProfileId = field(
        default=None,
        metadata={
            "name": "UniqueProfileID",
            "type": "Element",
        },
    )
    profile_data_filter: None | ProfileDataFilter1 = field(
        default=None,
        metadata={
            "name": "ProfileDataFilter",
            "type": "Element",
        },
    )
    parent_profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ParentProfileID",
            "type": "Attribute",
        },
    )
    parent_summary: bool = field(
        default=False,
        metadata={
            "name": "ParentSummary",
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
    parent_level_to_return: TypeParentProfileLevel = field(
        default=TypeParentProfileLevel.AGENCY,
        metadata={
            "name": "ParentLevelToReturn",
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
