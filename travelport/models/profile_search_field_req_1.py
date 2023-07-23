from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_2 import BaseReq2
from travelport.models.profile_search_modifiers_1 import ProfileSearchModifiers1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileSearchFieldReq1(BaseReq2):
    """
    Request to retrieve the fields and field groups owned by a specified agency.

    Parameters
    ----------
    profile_search_modifiers
    profile_id
        The ID of the agency or account that owns the fields/groups to be
        retrieved.
    """
    class Meta:
        name = "ProfileSearchFieldReq"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_search_modifiers: None | ProfileSearchModifiers1 = field(
        default=None,
        metadata={
            "name": "ProfileSearchModifiers",
            "type": "Element",
        }
    )
    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
