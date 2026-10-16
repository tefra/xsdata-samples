from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


class InstalmentBasisEnum(StrEnum):
    QUARTERLY = "Quarterly"
    ANNUAL = "Annual"
    HALF_YEARLY = "Half-yearly"
    BESPOKE = "Bespoke"
