from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_5 import BaseReq5
from travelport.models.profile_child_search_req_hierarchy_type_2 import (
    ProfileChildSearchReqHierarchyType2,
)
from travelport.models.profile_search_modifiers_2 import (
    ProfileSearchModifiers2,
)
from travelport.models.provisioning_code_profile_type_2 import (
    ProvisioningCodeProfileType2,
)
from travelport.models.unique_profile_id_profile_type_2 import (
    UniqueProfileIdProfileType2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class ProfileChildSearchReq2(BaseReq5):
    """
    Request to allow a user to retrieve the immediate children of a given
    profile.

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
    organization_name
        Name of the organization to filter for.
    given_name
    surname
    profile_search_modifiers
    hierarchy_type
        The type of hierarchy in which to search for children. If not
        specified search result will include profiles of all types.
    include_agents_and_travelers
        Indicator to include or exclude Travelers and Agent profiles when
        doing a this search.  The default is false, no Travelers or Agents
        will be returned.
    """

    class Meta:
        name = "ProfileChildSearchReq"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Element",
        },
    )
    provisioning_code: None | ProfileChildSearchReq2.ProvisioningCode = field(
        default=None,
        metadata={
            "name": "ProvisioningCode",
            "type": "Element",
        },
    )
    unique_profile_id: None | ProfileChildSearchReq2.UniqueProfileId = field(
        default=None,
        metadata={
            "name": "UniqueProfileID",
            "type": "Element",
        },
    )
    organization_name: None | str = field(
        default=None,
        metadata={
            "name": "OrganizationName",
            "type": "Element",
        },
    )
    given_name: None | str = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Element",
        },
    )
    surname: None | str = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Element",
        },
    )
    profile_search_modifiers: None | ProfileSearchModifiers2 = field(
        default=None,
        metadata={
            "name": "ProfileSearchModifiers",
            "type": "Element",
        },
    )
    hierarchy_type: None | ProfileChildSearchReqHierarchyType2 = field(
        default=None,
        metadata={
            "name": "HierarchyType",
            "type": "Attribute",
        },
    )
    include_agents_and_travelers: bool = field(
        default=False,
        metadata={
            "name": "IncludeAgentsAndTravelers",
            "type": "Attribute",
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
