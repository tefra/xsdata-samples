from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeHierarchyOverrideType(Enum):
    """
    Profile types that are used in default and override profiles on a hierarchy.
    """

    ACCOUNT = "Account"
    TRAVELER = "Traveler"
