from enum import Enum

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


class MaintenanceTypeEnum(Enum):
    VISIT = "Visit"
    EXTENDED = "Extended"
    GUARANTEE = "Guarantee"
