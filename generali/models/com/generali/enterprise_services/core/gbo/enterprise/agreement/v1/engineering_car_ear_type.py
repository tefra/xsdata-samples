from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.amount_type import (
    AmountType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.numeric_type import (
    NumericType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class EngineeringCarEarType:
    insured_values_md: AmountType | None = field(
        default=None,
        metadata={
            "name": "InsuredValuesMD",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    rate_md: NumericType | None = field(
        default=None,
        metadata={
            "name": "RateMD",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    insured_values_cpm_cpe_mb: AmountType | None = field(
        default=None,
        metadata={
            "name": "InsuredValuesCpmCpeMB",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    rate_cpm_cpe_mb: NumericType | None = field(
        default=None,
        metadata={
            "name": "RateCpmCpeMB",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    insured_values_mdother: AmountType | None = field(
        default=None,
        metadata={
            "name": "InsuredValuesMDOther",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    rate_mdother: NumericType | None = field(
        default=None,
        metadata={
            "name": "RateMDOther",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    insured_values_alop_dsu: AmountType | None = field(
        default=None,
        metadata={
            "name": "InsuredValuesAlopDsu",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    months_alop_dsu: NumericType | None = field(
        default=None,
        metadata={
            "name": "MonthsAlopDsu",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    calc_basis_alop_dsu_value: AmountType | None = field(
        default=None,
        metadata={
            "name": "CalcBasisAlopDsuValue",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    calc_basis_alop_dsu_pc: AmountType | None = field(
        default=None,
        metadata={
            "name": "CalcBasisAlopDsuPC",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    rate_alop_dsu: NumericType | None = field(
        default=None,
        metadata={
            "name": "RateAlopDsu",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    mflalop_dsu_pc: AmountType | None = field(
        default=None,
        metadata={
            "name": "MFLAlopDsuPC",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    deductible_mdother_value: AmountType | None = field(
        default=None,
        metadata={
            "name": "DeductibleMDOtherValue",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    deductible_days_alop_dsu: NumericType | None = field(
        default=None,
        metadata={
            "name": "DeductibleDaysAlopDsu",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    mflmachinery: AmountType | None = field(
        default=None,
        metadata={
            "name": "MFLMachinery",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    mflproject_pc: AmountType | None = field(
        default=None,
        metadata={
            "name": "MFLProjectPC",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    mflmdother_value: AmountType | None = field(
        default=None,
        metadata={
            "name": "MFLMDOtherValue",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    mflmdother_pc: AmountType | None = field(
        default=None,
        metadata={
            "name": "MFLMDOtherPC",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    deductible_project: AmountType | None = field(
        default=None,
        metadata={
            "name": "DeductibleProject",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
