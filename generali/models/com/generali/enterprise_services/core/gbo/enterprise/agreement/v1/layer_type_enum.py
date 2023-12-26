from enum import Enum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


class LayerTypeEnum(Enum):
    PRIMARY = "Primary"
    EXCESS = "Excess"
    QUOTA_SHARE = "QuotaShare"
