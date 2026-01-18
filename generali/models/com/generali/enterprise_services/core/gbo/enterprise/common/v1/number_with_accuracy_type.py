from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.numeric_type import (
    NumericType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.accuracy_code_list import (
    AccuracyCodeList,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class NumberWithAccuracyType(NumericType):
    accuracy: AccuracyCodeList | None = field(
        default=None,
        metadata={
            "name": "Accuracy",
            "type": "Attribute",
        },
    )
