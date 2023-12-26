from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofileCommon_v30_0"


class TypeProfileEntityStatusWithDelete1(Enum):
    """
    Specify whether the change is to update or delete the field.
    """

    DELETED = "Deleted"
    ACTIVE = "Active"
    INACTIVE = "Inactive"
