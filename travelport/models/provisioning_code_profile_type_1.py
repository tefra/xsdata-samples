from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class ProvisioningCodeProfileType1(StrEnum):
    AGENCY = "Agency"
    BRANCH_GROUP = "BranchGroup"
    BRANCH = "Branch"
    AGENT = "Agent"
