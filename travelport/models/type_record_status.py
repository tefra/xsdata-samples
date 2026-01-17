from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeRecordStatus(Enum):
    """
    Information on whether the Universal Record is Current, Past ,
    Cancelled or Any status.
    """

    ALL = "All"
    PAST = "Past"
    CURRENT = "Current"
    CANCELED = "Canceled"
    UNKNOWN = "Unknown"
