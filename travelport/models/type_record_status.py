from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeRecordStatus(StrEnum):
    """
    Information on whether the Universal Record is Current, Past ,
    Cancelled or Any status.
    """

    ALL = "All"
    PAST = "Past"
    CURRENT = "Current"
    CANCELED = "Canceled"
    UNKNOWN = "Unknown"
