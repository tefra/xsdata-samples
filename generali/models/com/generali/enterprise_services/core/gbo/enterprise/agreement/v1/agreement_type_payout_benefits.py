from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.payout_benefit import (
    PayoutBenefit,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class AgreementTypePayoutBenefits:
    class Meta:
        global_type = False

    payout_benefit: list[PayoutBenefit] = field(
        default_factory=list,
        metadata={
            "name": "PayoutBenefit",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
