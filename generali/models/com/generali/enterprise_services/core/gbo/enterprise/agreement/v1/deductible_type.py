from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.amount_type import (
    AmountType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_identified_component_type import (
    BaseIdentifiedComponentType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.code_description_type import (
    CodeDescriptionType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.value_type import (
    ValueType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.deductible_type_deductible_type import (
    DeductibleTypeDeductibleType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.deductible_type_restricted_to_geography import (
    DeductibleTypeRestrictedToGeography,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class DeductibleType(BaseIdentifiedComponentType):
    value: ValueType | None = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    basis: CodeDescriptionType | None = field(
        default=None,
        metadata={
            "name": "Basis",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    value_applies_to: CodeDescriptionType | None = field(
        default=None,
        metadata={
            "name": "ValueAppliesTo",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    restricted_to_geography: DeductibleTypeRestrictedToGeography | None = (
        field(
            default=None,
            metadata={
                "name": "RestrictedToGeography",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            },
        )
    )
    deductible_type: DeductibleTypeDeductibleType = field(
        default=DeductibleTypeDeductibleType.MAIN,
        metadata={
            "name": "DeductibleType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    maximum: AmountType | None = field(
        default=None,
        metadata={
            "name": "Maximum",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    minimum: AmountType | None = field(
        default=None,
        metadata={
            "name": "Minimum",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    separate_deductible: bool | None = field(
        default=None,
        metadata={
            "name": "SeparateDeductible",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    grouped: bool = field(
        default=False,
        metadata={
            "name": "Grouped",
            "type": "Attribute",
        },
    )
