from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofileCommon_v30_0"


class TypeProfileType2(StrEnum):
    """
    A type for unique party identifiers of any party role.
    """

    AGENCY_GROUP = "AgencyGroup"
    AGENCY = "Agency"
    BRANCH_GROUP = "BranchGroup"
    BRANCH = "Branch"
    AGENT = "Agent"
    ACCOUNT = "Account"
    TRAVELER_GROUP = "TravelerGroup"
    TRAVELER = "Traveler"
