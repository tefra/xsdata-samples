from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


class EmailNotificationRecipients3(Enum):
    ALL = "All"
    DEFAULT = "Default"
    SPECIFIC = "Specific"
