from enum import Enum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


class PolicyTypeEnum(Enum):
    ADMITTED = "Admitted"
    FREEDOM_OF_SERVICE = "FreedomOfService"
    NON_ADMITTED = "NonAdmitted"
    MASTER = "Master"
    LAYER = "Layer"
