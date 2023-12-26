from dataclasses import dataclass, field
from typing import Optional
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
    calculated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Calculated",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    value: Optional[ValueTypeDeduction] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    applies_to_premium_type: Optional[DeductionApplyToEnum] = field(
        default=None,
        metadata={
            "name": "AppliesToPremiumType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    value_type: Optional[PremiumValueEnum] = field(
        default=None,
        metadata={
            "name": "ValueType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    deduction_type: Optional[CodeDescriptionType] = field(
        default=None,
        metadata={
            "name": "DeductionType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    time_applied: Optional[TimeAppliedEnum] = field(
        default=None,
        metadata={
            "name": "TimeApplied",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    applied_deductions: Optional[AppliedDeductionsType] = field(
        default=None,
        metadata={
            "name": "AppliedDeductions",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
