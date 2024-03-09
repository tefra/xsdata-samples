from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeCreateHierarchyLevel(Enum):
    """
    Profile types that are used in creating a hiearchy.
    """

    BRANCH_GROUP = "BranchGroup"
    TRAVELER_GROUP = "TravelerGroup"
