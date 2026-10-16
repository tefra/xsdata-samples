from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


class PolicyTypeEnum(StrEnum):
    ADMITTED = "Admitted"
    FREEDOM_OF_SERVICE = "FreedomOfService"
    NON_ADMITTED = "NonAdmitted"
    MASTER = "Master"
    LAYER = "Layer"
