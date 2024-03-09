from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_5 import BaseReq5
from travelport.models.profile_search_modifiers_2 import (
    ProfileSearchModifiers2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileSearchFieldReq2(BaseReq5):
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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_search_modifiers: None | ProfileSearchModifiers2 = field(
        default=None,
        metadata={
            "name": "ProfileSearchModifiers",
            "type": "Element",
        },
    )
    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        },
    )
