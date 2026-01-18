from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.amount_type import (
    AmountType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.numeric_type import (
    NumericType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass(kw_only=True)
class EngineeringCarEarType:
    insured_values_md: None | AmountType = field(
        default=None,
        metadata={
            "name": "InsuredValuesMD",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    rate_md: None | NumericType = field(
        default=None,
        metadata={
            "name": "RateMD",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    insured_values_cpm_cpe_mb: None | AmountType = field(
        default=None,
        metadata={
            "name": "InsuredValuesCpmCpeMB",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    rate_cpm_cpe_mb: None | NumericType = field(
        default=None,
        metadata={
            "name": "RateCpmCpeMB",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    insured_values_mdother: None | AmountType = field(
        default=None,
        metadata={
            "name": "InsuredValuesMDOther",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    rate_mdother: None | NumericType = field(
        default=None,
        metadata={
            "name": "RateMDOther",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    insured_values_alop_dsu: None | AmountType = field(
        default=None,
        metadata={
            "name": "InsuredValuesAlopDsu",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    months_alop_dsu: None | NumericType = field(
        default=None,
        metadata={
            "name": "MonthsAlopDsu",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    calc_basis_alop_dsu_value: None | AmountType = field(
        default=None,
        metadata={
            "name": "CalcBasisAlopDsuValue",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    calc_basis_alop_dsu_pc: None | AmountType = field(
        default=None,
        metadata={
            "name": "CalcBasisAlopDsuPC",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    rate_alop_dsu: None | NumericType = field(
        default=None,
        metadata={
            "name": "RateAlopDsu",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    mflalop_dsu_pc: None | AmountType = field(
        default=None,
        metadata={
            "name": "MFLAlopDsuPC",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    deductible_mdother_value: None | AmountType = field(
        default=None,
        metadata={
            "name": "DeductibleMDOtherValue",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    deductible_days_alop_dsu: None | NumericType = field(
        default=None,
        metadata={
            "name": "DeductibleDaysAlopDsu",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    mflmachinery: None | AmountType = field(
        default=None,
        metadata={
            "name": "MFLMachinery",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    mflproject_pc: None | AmountType = field(
        default=None,
        metadata={
            "name": "MFLProjectPC",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    mflmdother_value: None | AmountType = field(
        default=None,
        metadata={
            "name": "MFLMDOtherValue",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    mflmdother_pc: None | AmountType = field(
        default=None,
        metadata={
            "name": "MFLMDOtherPC",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    deductible_project: None | AmountType = field(
        default=None,
        metadata={
            "name": "DeductibleProject",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
