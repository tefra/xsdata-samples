from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_identified_component_type import (
    BaseIdentifiedComponentType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.code_description_type import (
    CodeDescriptionType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.value_type_deduction import (
    ValueTypeDeduction,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.applied_deductions_type import (
    AppliedDeductionsType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.premium_value_enum import (
    PremiumValueEnum,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.time_applied_enum import (
    TimeAppliedEnum,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.deduction_apply_to_enum import (
    DeductionApplyToEnum,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class DeductionType(BaseIdentifiedComponentType):
    calculated: bool | None = field(
        default=None,
        metadata={
            "name": "Calculated",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    value: ValueTypeDeduction | None = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    applies_to_premium_type: DeductionApplyToEnum | None = field(
        default=None,
        metadata={
            "name": "AppliesToPremiumType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    value_type: PremiumValueEnum | None = field(
        default=None,
        metadata={
            "name": "ValueType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    deduction_type: CodeDescriptionType | None = field(
        default=None,
        metadata={
            "name": "DeductionType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    time_applied: TimeAppliedEnum | None = field(
        default=None,
        metadata={
            "name": "TimeApplied",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    applied_deductions: AppliedDeductionsType | None = field(
        default=None,
        metadata={
            "name": "AppliedDeductions",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
