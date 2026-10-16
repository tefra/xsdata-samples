from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


class TypeAgencyProfileLevel3(StrEnum):
    """
    Profile levels in the Agency Hierarchy.
    """

    AGENCY = "Agency"
    BRANCH = "Branch"
    BRANCH_GROUP = "BranchGroup"
    AGENT = "Agent"
