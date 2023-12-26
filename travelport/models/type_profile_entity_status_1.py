from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofileCommon_v30_0"


class TypeProfileEntityStatus1(Enum):
    """Status of the given profile/entity.

    Any profile with a status other than Active cannot perform most
    transactions.
    """

    ACTIVE = "Active"
    INACTIVE = "Inactive"
