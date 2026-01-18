from __future__ import annotations

from dataclasses import dataclass, field

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
    insured_risk_element: RiskElementRoleType | None = field(
        default=None,
        metadata={
            "name": "InsuredRiskElement",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    validity: TimePeriodType | None = field(
        default=None,
        metadata={
            "name": "Validity",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    classification_code: ClassificationType | None = field(
        default=None,
        metadata={
            "name": "ClassificationCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    engineering_car_ear: EngineeringCarEarType | None = field(
        default=None,
        metadata={
            "name": "EngineeringCarEar",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    engineering_mb: EngineeringMbType | None = field(
        default=None,
        metadata={
            "name": "EngineeringMb",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    engineering_pm: EngineeringPmType | None = field(
        default=None,
        metadata={
            "name": "EngineeringPm",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
