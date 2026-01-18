from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SharedUsageEnumeration(Enum):
    SINGLE_USER = "singleUser"
    CONCURRENT_USERS = "concurrentUsers"
    CONCURRENT_DESIGNATED_USERS = "concurrentDesignatedUsers"
