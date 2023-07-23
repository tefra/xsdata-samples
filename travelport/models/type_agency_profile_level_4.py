from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


class TypeAgencyProfileLevel4(Enum):
    """
    Profile levels in the Agency Hierarchy.
    """
    AGENCY = "Agency"
    BRANCH = "Branch"
    BRANCH_GROUP = "BranchGroup"
    AGENT = "Agent"
