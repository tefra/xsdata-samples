from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeUpdateAction2(StrEnum):
    """
    Specify whether the change is to update or delete the field.
    """

    UPDATE = "Update"
    DELETE = "Delete"
