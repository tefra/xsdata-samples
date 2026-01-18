from __future__ import annotations

from enum import Enum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


class InsurerCapabilityType(Enum):
    CEDANT = "Cedant"
    FRONTING = "Fronting"
    PRODUCING = "Producing"
    REINSURER = "Reinsurer"
    COINSURER = "Coinsurer"
