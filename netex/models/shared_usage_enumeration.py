from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SharedUsageEnumeration(StrEnum):
    SINGLE_USER = "singleUser"
    CONCURRENT_USERS = "concurrentUsers"
    CONCURRENT_DESIGNATED_USERS = "concurrentDesignatedUsers"
