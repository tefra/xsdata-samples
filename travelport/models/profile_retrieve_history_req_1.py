from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_2 import BaseReq2
from travelport.models.profile_history_retrieve_criteria_1 import (
    ProfileHistoryRetrieveCriteria1,
)
from travelport.models.profile_search_modifiers_1 import (
    ProfileSearchModifiers1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class ProfileRetrieveHistoryReq1(BaseReq2):
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
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_id: int = field(
        metadata={
            "name": "ProfileID",
            "type": "Element",
            "required": True,
        }
    )
    profile_history_retrieve_criteria: (
        None | ProfileHistoryRetrieveCriteria1
    ) = field(
        default=None,
        metadata={
            "name": "ProfileHistoryRetrieveCriteria",
            "type": "Element",
        },
    )
    profile_search_modifiers: None | ProfileSearchModifiers1 = field(
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
