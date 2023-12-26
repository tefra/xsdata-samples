from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.classification_type import (
    ClassificationType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.time_period_type import (
    TimePeriodType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.engineering_car_ear_type import (
    EngineeringCarEarType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.engineering_mb_type import (
    EngineeringMbType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.engineering_pm_type import (
    EngineeringPmType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.risk_involvement import (
    RiskInvolvement,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.risk_element_role_type import (
    RiskElementRoleType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class RiskElementInvolvementType(RiskInvolvement):
    insured_risk_element: Optional[RiskElementRoleType] = field(
        default=None,
        metadata={
            "name": "InsuredRiskElement",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    validity: Optional[TimePeriodType] = field(
        default=None,
        metadata={
            "name": "Validity",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    classification_code: Optional[ClassificationType] = field(
        default=None,
        metadata={
            "name": "ClassificationCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    engineering_car_ear: Optional[EngineeringCarEarType] = field(
        default=None,
        metadata={
            "name": "EngineeringCarEar",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    engineering_mb: Optional[EngineeringMbType] = field(
        default=None,
        metadata={
            "name": "EngineeringMb",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    engineering_pm: Optional[EngineeringPmType] = field(
        default=None,
        metadata={
            "name": "EngineeringPm",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
