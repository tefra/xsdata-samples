from enum import Enum

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


class InsuredInvolvementType(Enum):
    PRINCIPAL = "Principal"
    POLICY_HOLDER = "PolicyHolder"
    ADDITIONAL = "Additional"
    LOCAL = "Local"
