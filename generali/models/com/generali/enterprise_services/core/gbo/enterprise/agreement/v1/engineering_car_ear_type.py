from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.amount_type import AmountType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


@dataclass
class EngineeringCarEarType:
    insured_values_md: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "InsuredValuesMD",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    rate_md: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RateMD",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    insured_values_cpm_cpe_mb: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "InsuredValuesCpmCpeMB",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    rate_cpm_cpe_mb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RateCpmCpeMB",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    insured_values_mdother: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "InsuredValuesMDOther",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    rate_mdother: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RateMDOther",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    insured_values_alop_dsu: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "InsuredValuesAlopDsu",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    months_alop_dsu: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MonthsAlopDsu",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    calc_basis_alop_dsu_value: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "CalcBasisAlopDsuValue",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    calc_basis_alop_dsu_pc: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "CalcBasisAlopDsuPC",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    rate_alop_dsu: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RateAlopDsu",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    mflalop_dsu_pc: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "MFLAlopDsuPC",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    deductible_mdother_value: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "DeductibleMDOtherValue",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    deductible_days_alop_dsu: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DeductibleDaysAlopDsu",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    mflmachinery: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "MFLMachinery",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    mflproject_pc: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "MFLProjectPC",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    mflmdother_value: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "MFLMDOtherValue",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    mflmdother_pc: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "MFLMDOtherPC",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    deductible_project: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "DeductibleProject",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
