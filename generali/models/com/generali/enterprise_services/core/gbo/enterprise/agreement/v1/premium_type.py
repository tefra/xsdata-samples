from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from xsdata.models.datatype import XmlDate
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.amount_type import AmountType
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.idtype import Idtype
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import TextType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.instalment_term_enum import InstalmentTermEnum
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.premium_type_collected_amounts import PremiumTypeCollectedAmounts
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.premium_type_premium_allocations import PremiumTypePremiumAllocations
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.premium_value_enum import PremiumValueEnum
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.warranty_enum import WarrantyEnum

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


@dataclass
class PremiumType:
    is_minimum: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMinimum",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    days_of_credit: Optional[int] = field(
        default=None,
        metadata={
            "name": "DaysOfCredit",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    catnat: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "CATNAT",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    gareat: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "GAREAT",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    gross: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "Gross",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    net: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "Net",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    technical: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "Technical",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    number_of_installments: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfInstallments",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    description: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    identifier: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    reserve_held: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "ReserveHeld",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    settlement_due_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SettlementDueDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    payment: Optional[PremiumValueEnum] = field(
        default=None,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    warranty: Optional[WarrantyEnum] = field(
        default=None,
        metadata={
            "name": "Warranty",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    instalment_term: Optional[InstalmentTermEnum] = field(
        default=None,
        metadata={
            "name": "InstalmentTerm",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    premium_allocations: Optional[PremiumTypePremiumAllocations] = field(
        default=None,
        metadata={
            "name": "PremiumAllocations",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    collected_amounts: Optional[PremiumTypeCollectedAmounts] = field(
        default=None,
        metadata={
            "name": "CollectedAmounts",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    gwpshare: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "GWPShare",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    share_percentage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SharePercentage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    number_of_ptlayers: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfPTLayers",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
