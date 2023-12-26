from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.account_criteria_2 import AccountCriteria2
from travelport.models.agency_criteria_2 import AgencyCriteria2
from travelport.models.agency_group_criteria_2 import AgencyGroupCriteria2
from travelport.models.agent_criteria_2 import AgentCriteria2
from travelport.models.branch_criteria_2 import BranchCriteria2
from travelport.models.branch_group_criteria_2 import BranchGroupCriteria2
from travelport.models.traveler_criteria_3 import TravelerCriteria3
from travelport.models.traveler_group_criteria_2 import TravelerGroupCriteria2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileTypeSearch2:
    """
    Specifies which type of profile to be searched on and includes modifiers for
    each type.
    """

    class Meta:
        name = "ProfileTypeSearch"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    agency_group_criteria: None | AgencyGroupCriteria2 = field(
        default=None,
        metadata={
            "name": "AgencyGroupCriteria",
            "type": "Element",
        },
    )
    agency_criteria: None | AgencyCriteria2 = field(
        default=None,
        metadata={
            "name": "AgencyCriteria",
            "type": "Element",
        },
    )
    branch_criteria: None | BranchCriteria2 = field(
        default=None,
        metadata={
            "name": "BranchCriteria",
            "type": "Element",
        },
    )
    branch_group_criteria: None | BranchGroupCriteria2 = field(
        default=None,
        metadata={
            "name": "BranchGroupCriteria",
            "type": "Element",
        },
    )
    agent_criteria: None | AgentCriteria2 = field(
        default=None,
        metadata={
            "name": "AgentCriteria",
            "type": "Element",
        },
    )
    account_criteria: None | AccountCriteria2 = field(
        default=None,
        metadata={
            "name": "AccountCriteria",
            "type": "Element",
        },
    )
    traveler_criteria: None | TravelerCriteria3 = field(
        default=None,
        metadata={
            "name": "TravelerCriteria",
            "type": "Element",
        },
    )
    traveler_group_criteria: None | TravelerGroupCriteria2 = field(
        default=None,
        metadata={
            "name": "TravelerGroupCriteria",
            "type": "Element",
        },
    )
