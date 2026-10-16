from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class EmailNotificationRecipients1(StrEnum):
    ALL = "All"
    DEFAULT = "Default"
    SPECIFIC = "Specific"
