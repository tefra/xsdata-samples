from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.amount_type import (
    AmountType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.percent_type import (
    PercentType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import (
    TextType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_component_type import (
    BaseComponentType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class PremiumFactorType(BaseComponentType):
    amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    description: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    percentage: Optional[PercentType] = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
