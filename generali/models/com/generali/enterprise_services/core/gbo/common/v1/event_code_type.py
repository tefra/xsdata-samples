from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


class EventCodeType(Enum):
    CREATED = "Created"
    UPDATED = "Updated"
    DELETED = "Deleted"
