from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.amount_type import (
    AmountType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.date_time_type import (
    DateTimeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_reference_component_type import (
    BaseReferenceComponentType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass(kw_only=True)
class PaymentTransactionType(BaseReferenceComponentType):
    payment_date: None | DateTimeType = field(
        default=None,
        metadata={
            "name": "PaymentDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    payment_due_date: None | DateTimeType = field(
        default=None,
        metadata={
            "name": "PaymentDueDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    amount: list[AmountType] = field(
        default_factory=list,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
