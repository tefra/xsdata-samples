from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class ProvisioningCodeProfileType2(StrEnum):
    AGENCY = "Agency"
    BRANCH_GROUP = "BranchGroup"
    BRANCH = "Branch"
    AGENT = "Agent"
