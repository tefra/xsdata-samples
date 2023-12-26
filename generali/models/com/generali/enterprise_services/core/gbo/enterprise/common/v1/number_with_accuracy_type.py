from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.accuracy_code_list import (
    AccuracyCodeList,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class NumberWithAccuracyType:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    accuracy: Optional[AccuracyCodeList] = field(
        default=None,
        metadata={
            "name": "Accuracy",
            "type": "Attribute",
        },
    )
