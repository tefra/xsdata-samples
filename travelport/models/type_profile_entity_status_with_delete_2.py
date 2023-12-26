from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


class TypeProfileEntityStatusWithDelete2(Enum):
    """
    Specify whether the change is to update or delete the field.
    """

    DELETED = "Deleted"
    ACTIVE = "Active"
    INACTIVE = "Inactive"
