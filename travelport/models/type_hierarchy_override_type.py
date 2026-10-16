from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeHierarchyOverrideType(StrEnum):
    """
    Profile types that are used in default and override profiles on a
    hierarchy.
    """

    ACCOUNT = "Account"
    TRAVELER = "Traveler"
