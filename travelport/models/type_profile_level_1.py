from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeProfileLevel1(StrEnum):
    """
    The type of the profile or profile template.
    """

    AGENCY = "Agency"
    BRANCH = "Branch"
    BRANCH_GROUP = "BranchGroup"
    AGENT = "Agent"
    ACCOUNT = "Account"
    TRAVELER_GROUP = "TravelerGroup"
    TRAVELER = "Traveler"
