from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_5 import BaseReq5
from travelport.models.profile_search_2 import ProfileSearch2
from travelport.models.profile_search_modifiers_2 import (
    ProfileSearchModifiers2,
)
from travelport.models.profile_type_search_2 import ProfileTypeSearch2
from travelport.models.type_profile_type_7 import TypeProfileType7

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileSearchReq2(BaseReq5):
    """Request to search for profiles of a specified type, within a specified
    parent.

    No more than 5 parameters can be specified for a given search
    request (in addition to ProfileSearchModifiers and a parent ID and
    Type). Returns any profiles that match all the parameters specified.

    Parameters
    ----------
    profile_type_search
    profile_search
    profile_search_modifiers
    profile_type
        Limit the search to specific profile type.
    profile_parent_id
        The ID of the profile parent or ancestor to search within.This will
        be used to constrain the scope of the search to a given account,
        branch, etc. If none is specified, the system will infer the scope
        based on the user's permissions and emulation.
    return_parent_summary
        If true, the response will include profile summary information from
        this profile's parents.
    search_token
        Search token to retrieve search result from cache, if present.
    """

    class Meta:
        name = "ProfileSearchReq"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_type_search: None | ProfileTypeSearch2 = field(
        default=None,
        metadata={
            "name": "ProfileTypeSearch",
            "type": "Element",
        },
    )
    profile_search: None | ProfileSearch2 = field(
        default=None,
        metadata={
            "name": "ProfileSearch",
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
    profile_type: None | TypeProfileType7 = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        },
    )
    profile_parent_id: None | object = field(
        default=None,
        metadata={
            "name": "ProfileParentID",
            "type": "Attribute",
        },
    )
    return_parent_summary: bool = field(
        default=False,
        metadata={
            "name": "ReturnParentSummary",
            "type": "Attribute",
        },
    )
    search_token: None | str = field(
        default=None,
        metadata={
            "name": "SearchToken",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
