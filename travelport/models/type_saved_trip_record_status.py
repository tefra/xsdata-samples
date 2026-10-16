from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


class TypeSavedTripRecordStatus(StrEnum):
    """
    Specifies the status of the Saved Trip record.
    """

    ALL = "All"
    PAST = "Past"
    CURRENT = "Current"
