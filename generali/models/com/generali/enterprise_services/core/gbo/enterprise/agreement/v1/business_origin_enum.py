from __future__ import annotations

from enum import Enum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


class BusinessOriginEnum(Enum):
    NEW_BUSINESS = "NewBusiness"
    RENEWAL = "Renewal"
