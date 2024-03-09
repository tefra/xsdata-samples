from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.numeric_type import (
    NumericType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.code_description_type import (
    CodeDescriptionType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.risk_element_type import (
    RiskElementType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class LiabilityType(RiskElementType):
    rating: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "Rating",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    share_capital: Optional[NumericType] = field(
        default=None,
        metadata={
            "name": "ShareCapital",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    liablity_type: Optional[CodeDescriptionType] = field(
        default=None,
        metadata={
            "name": "LiablityType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
