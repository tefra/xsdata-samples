from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.account_criteria_1 import AccountCriteria1
from travelport.models.agency_criteria_1 import AgencyCriteria1
from travelport.models.agency_group_criteria_1 import AgencyGroupCriteria1
from travelport.models.agent_criteria_1 import AgentCriteria1
from travelport.models.branch_criteria_1 import BranchCriteria1
from travelport.models.branch_group_criteria_1 import BranchGroupCriteria1
from travelport.models.traveler_criteria_2 import TravelerCriteria2
from travelport.models.traveler_group_criteria_1 import TravelerGroupCriteria1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileTypeSearch1:
    """
    Specifies which type of profile to be searched on and includes
    modifiers for each type.
    """

    class Meta:
        name = "ProfileTypeSearch"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    agency_group_criteria: None | AgencyGroupCriteria1 = field(
        default=None,
        metadata={
            "name": "AgencyGroupCriteria",
            "type": "Element",
        },
    )
    agency_criteria: None | AgencyCriteria1 = field(
        default=None,
        metadata={
            "name": "AgencyCriteria",
            "type": "Element",
        },
    )
    branch_criteria: None | BranchCriteria1 = field(
        default=None,
        metadata={
            "name": "BranchCriteria",
            "type": "Element",
        },
    )
    branch_group_criteria: None | BranchGroupCriteria1 = field(
        default=None,
        metadata={
            "name": "BranchGroupCriteria",
            "type": "Element",
        },
    )
    agent_criteria: None | AgentCriteria1 = field(
        default=None,
        metadata={
            "name": "AgentCriteria",
            "type": "Element",
        },
    )
    account_criteria: None | AccountCriteria1 = field(
        default=None,
        metadata={
            "name": "AccountCriteria",
            "type": "Element",
        },
    )
    traveler_criteria: None | TravelerCriteria2 = field(
        default=None,
        metadata={
            "name": "TravelerCriteria",
            "type": "Element",
        },
    )
    traveler_group_criteria: None | TravelerGroupCriteria1 = field(
        default=None,
        metadata={
            "name": "TravelerGroupCriteria",
            "type": "Element",
        },
    )
