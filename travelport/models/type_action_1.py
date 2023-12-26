from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class TypeAction1(Enum):
    """
    Specify whether the change is to add, update, or delete the field.
    """

    ADD = "Add"
    UPDATE = "Update"
    DELETE = "Delete"
