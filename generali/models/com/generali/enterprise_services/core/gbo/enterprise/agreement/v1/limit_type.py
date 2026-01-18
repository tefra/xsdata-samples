from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.amount_type import (
    AmountType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.numeric_type import (
    NumericType,
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
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.indemnity_type import (
    IndemnityType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.limit_type_restricted_to_geography import (
    LimitTypeRestrictedToGeography,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.limit_type_type import (
    LimitTypeType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class LimitType(BaseIdentifiedComponentType):
    value: None | ValueType = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    maximum: None | AmountType = field(
        default=None,
        metadata={
            "name": "Maximum",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    minimum: None | AmountType = field(
        default=None,
        metadata={
            "name": "Minimum",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    basis: None | CodeDescriptionType = field(
        default=None,
        metadata={
            "name": "Basis",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    time_specification: None | NumericType = field(
        default=None,
        metadata={
            "name": "TimeSpecification",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    restricted_to_geography: None | LimitTypeRestrictedToGeography = field(
        default=None,
        metadata={
            "name": "RestrictedToGeography",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    value_applies_to: None | CodeDescriptionType = field(
        default=None,
        metadata={
            "name": "ValueAppliesTo",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    type_value: None | LimitTypeType = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    indemnity: None | IndemnityType = field(
        default=None,
        metadata={
            "name": "Indemnity",
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
