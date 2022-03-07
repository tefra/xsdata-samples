from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.amount_type import AmountType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.accuracy_code_list import AccuracyCodeList

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"


@dataclass
class AmountWithAccuracyType(AmountType):
    accuracy: Optional[AccuracyCodeList] = field(
        default=None,
        metadata={
            "name": "Accuracy",
            "type": "Attribute",
        }
    )
