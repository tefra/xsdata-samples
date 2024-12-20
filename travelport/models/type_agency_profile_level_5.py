from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


class TypeAgencyProfileLevel5(Enum):
    """
    Profile levels in the Agency Hierarchy.
    """

    AGENCY = "Agency"
    BRANCH = "Branch"
    BRANCH_GROUP = "BranchGroup"
    AGENT = "Agent"
