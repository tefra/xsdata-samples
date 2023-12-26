from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class TypeUpdateAction1(Enum):
    """
    Specify whether the change is to update or delete the field.
    """

    UPDATE = "Update"
    DELETE = "Delete"
