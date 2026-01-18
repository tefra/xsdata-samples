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


@dataclass
class EngineeringMbType:
    machinery_manufacturer: str | None = field(
        default=None,
        metadata={
            "name": "MachineryManufacturer",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    machinery_model: str | None = field(
        default=None,
        metadata={
            "name": "MachineryModel",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    machinery_serial_number: str | None = field(
        default=None,
        metadata={
            "name": "MachinerySerialNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    insured_values_machinery: AmountType | None = field(
        default=None,
        metadata={
            "name": "InsuredValuesMachinery",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    rate_mbmachinery: NumericType | None = field(
        default=None,
        metadata={
            "name": "RateMBMachinery",
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
    rate_all_risks_machinery: NumericType | None = field(
        default=None,
        metadata={
            "name": "RateAllRisksMachinery",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    rate_mbbi: NumericType | None = field(
        default=None,
        metadata={
            "name": "RateMBBI",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    rate_all_risks_bi: NumericType | None = field(
        default=None,
        metadata={
            "name": "RateAllRisksBI",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    mflother: NumericType | None = field(
        default=None,
        metadata={
            "name": "MFLOther",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
