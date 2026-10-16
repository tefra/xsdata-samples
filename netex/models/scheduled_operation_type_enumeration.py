from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ScheduledOperationTypeEnumeration(StrEnum):
    SCHEDULED_SERVICE = "scheduledService"
    EVENT_BASED_SERVICE = "eventBasedService"
