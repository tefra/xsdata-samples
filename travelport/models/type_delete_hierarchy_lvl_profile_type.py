from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeDeleteHierarchyLvlProfileType(Enum):
    """
    A type for unique party identifiers of any party role.
    """

    BRANCH_GROUP = "BranchGroup"
    TRAVELER_GROUP = "TravelerGroup"
