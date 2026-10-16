from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


class InsurerCapabilityType(StrEnum):
    CEDANT = "Cedant"
    FRONTING = "Fronting"
    PRODUCING = "Producing"
    REINSURER = "Reinsurer"
    COINSURER = "Coinsurer"
