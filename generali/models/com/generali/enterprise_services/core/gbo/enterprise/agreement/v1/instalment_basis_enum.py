from enum import Enum

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


class InstalmentBasisEnum(Enum):
    QUARTERLY = "Quarterly"
    ANNUAL = "Annual"
    HALF_YEARLY = "Half-yearly"
    BESPOKE = "Bespoke"
