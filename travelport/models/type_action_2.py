from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeAction2(StrEnum):
    """
    Specify whether the change is to add, update, or delete the field.
    """

    ADD = "Add"
    UPDATE = "Update"
    DELETE = "Delete"
