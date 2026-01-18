from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.amount_type import (
    AmountType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.date_type import (
    DateType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.idtype import (
    Idtype,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.number_type import (
    NumberType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.percent_type import (
    PercentType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import (
    TextType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.instalment_term_enum import (
    InstalmentTermEnum,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.premium_type_collected_amounts import (
    PremiumTypeCollectedAmounts,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.premium_type_premium_allocations import (
    PremiumTypePremiumAllocations,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.premium_value_enum import (
    PremiumValueEnum,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.warranty_enum import (
    WarrantyEnum,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class PremiumType:
    is_minimum: bool | None = field(
        default=None,
        metadata={
            "name": "IsMinimum",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    days_of_credit: NumberType | None = field(
        default=None,
        metadata={
            "name": "DaysOfCredit",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    catnat: AmountType | None = field(
        default=None,
        metadata={
            "name": "CATNAT",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    gareat: AmountType | None = field(
        default=None,
        metadata={
            "name": "GAREAT",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    gross: AmountType | None = field(
        default=None,
        metadata={
            "name": "Gross",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    net: AmountType | None = field(
        default=None,
        metadata={
            "name": "Net",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    technical: AmountType | None = field(
        default=None,
        metadata={
            "name": "Technical",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    number_of_installments: NumberType | None = field(
        default=None,
        metadata={
            "name": "NumberOfInstallments",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    description: TextType | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    identifier: Idtype | None = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    reserve_held: AmountType | None = field(
        default=None,
        metadata={
            "name": "ReserveHeld",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    settlement_due_date: DateType | None = field(
        default=None,
        metadata={
            "name": "SettlementDueDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    payment: PremiumValueEnum | None = field(
        default=None,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    warranty: WarrantyEnum | None = field(
        default=None,
        metadata={
            "name": "Warranty",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    instalment_term: InstalmentTermEnum | None = field(
        default=None,
        metadata={
            "name": "InstalmentTerm",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    premium_allocations: PremiumTypePremiumAllocations | None = field(
        default=None,
        metadata={
            "name": "PremiumAllocations",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    collected_amounts: PremiumTypeCollectedAmounts | None = field(
        default=None,
        metadata={
            "name": "CollectedAmounts",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    gwpshare: AmountType | None = field(
        default=None,
        metadata={
            "name": "GWPShare",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    share_percentage: PercentType | None = field(
        default=None,
        metadata={
            "name": "SharePercentage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    number_of_ptlayers: NumberType | None = field(
        default=None,
        metadata={
            "name": "NumberOfPTLayers",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
