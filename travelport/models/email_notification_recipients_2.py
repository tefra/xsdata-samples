from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


class EmailNotificationRecipients2(Enum):
    ALL = "All"
    DEFAULT = "Default"
    SPECIFIC = "Specific"
