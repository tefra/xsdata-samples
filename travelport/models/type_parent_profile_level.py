from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofileCommon_v30_0"


class TypeParentProfileLevel(Enum):
    """
    Returns parent’s data up to specified hierarchy.

    Valid values are ‘Agency’, ‘AgencyGroup’, ‘BranchGroup’, ‘Branch’,
    ‘Account’ and ‘Traveler Group’.
    """

    AGENCY_GROUP = "AgencyGroup"
    AGENCY = "Agency"
    BRANCH_GROUP = "BranchGroup"
    BRANCH = "Branch"
    ACCOUNT = "Account"
    TRAVELER_GROUP = "TravelerGroup"
