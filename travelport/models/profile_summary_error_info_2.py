from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_error_info_5 import TypeErrorInfo5
from travelport.models.type_profile_type_7 import TypeProfileType7

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class ProfileSummaryErrorInfo2(TypeErrorInfo5):
    """
    Error information when a profile service fails and profile information
    is needed to be returned.

    The service failed because there profiles attached to the element being
    modified. This error info shows those profiles Up to the first 100
    profiles are shown.

    Parameters
    ----------
    profile_summary
    number_of_children
        The number of children that the profile attempted to being deleted
        has.
    """

    class Meta:
        name = "ProfileSummaryErrorInfo"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_summary: list[ProfileSummaryErrorInfo2.ProfileSummary] = field(
        default_factory=list,
        metadata={
            "name": "ProfileSummary",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 100,
        },
    )
    number_of_children: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfChildren",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class ProfileSummary:
        """
        Parameters
        ----------
        profile_id
            The system-assigned, unique ID of the profile.
        profile_type
            The type of profile this profile is for (e.g., branch, account,
            traveler). The profile type identifies which default
            attributes/elements (minimum data set) the system will insert.
        name
            Name given to the profile.  If a Traveler or Account, then this
            is a union of the person names.  For all other types it is the
            appropriate name.
        description
            Description of profile
        provisioning_code
            Provisioning code given to the profile if applicable.
        """

        profile_id: int = field(
            metadata={
                "name": "ProfileID",
                "type": "Attribute",
                "required": True,
            }
        )
        profile_type: TypeProfileType7 = field(
            metadata={
                "name": "ProfileType",
                "type": "Attribute",
                "required": True,
            }
        )
        name: str = field(
            metadata={
                "name": "Name",
                "type": "Attribute",
                "required": True,
            }
        )
        description: None | str = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Attribute",
            },
        )
        provisioning_code: None | str = field(
            default=None,
            metadata={
                "name": "ProvisioningCode",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 128,
            },
        )
