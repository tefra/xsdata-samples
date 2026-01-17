from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_5 import BaseReq5
from travelport.models.profile_history_retrieve_criteria_2 import (
    ProfileHistoryRetrieveCriteria2,
)
from travelport.models.profile_search_modifiers_2 import (
    ProfileSearchModifiers2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileRetrieveHistoryReq2(BaseReq5):
    """
    Request to retrieve history for the whole profile, a particular
    element, or a date range.

    Parameters
    ----------
    profile_id
        Specify the unique ID of the profile whose history is being
        retrieved.
    profile_history_retrieve_criteria
    profile_search_modifiers
    show_data_unmasked
        Set to true to show data unmasked in the profile history retrieve
        response. Requires special authorization.
    """

    class Meta:
        name = "ProfileRetrieveHistoryReq"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Element",
            "required": True,
        },
    )
    profile_history_retrieve_criteria: (
        None | ProfileHistoryRetrieveCriteria2
    ) = field(
        default=None,
        metadata={
            "name": "ProfileHistoryRetrieveCriteria",
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
    show_data_unmasked: bool = field(
        default=False,
        metadata={
            "name": "ShowDataUnmasked",
            "type": "Attribute",
        },
    )
