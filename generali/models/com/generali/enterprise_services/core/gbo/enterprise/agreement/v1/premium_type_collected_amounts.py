from dataclasses import dataclass, field
from typing import List
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.payment_transaction_type import (
    PaymentTransactionType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class PremiumTypeCollectedAmounts:
    class Meta:
        global_type = False

    collected_amount: List[PaymentTransactionType] = field(
        default_factory=list,
        metadata={
            "name": "CollectedAmount",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
