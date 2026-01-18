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
class EngineeringPmType:
    machinery_type: None | str = field(
        default=None,
        metadata={
            "name": "MachineryType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    insured_values_cpm_cpe_machinery: None | AmountType = field(
        default=None,
        metadata={
            "name": "InsuredValuesCpmCpeMachinery",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    rate_cpm_cpe_machinery: None | NumericType = field(
        default=None,
        metadata={
            "name": "RateCpmCpeMachinery",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    mflmachinery: None | NumericType = field(
        default=None,
        metadata={
            "name": "MFLMachinery",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
