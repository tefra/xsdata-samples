from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.date_time_type import (
    DateTimeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.idtype import (
    Idtype,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.number_type import (
    NumberType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.numeric_type import (
    NumericType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.percent_type import (
    PercentType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import (
    TextType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.agreement_type import (
    AgreementType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.clauses_type import (
    ClausesType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.cover_gbotype_cedants import (
    CoverGbotypeCedants,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.cover_gbotype_claims import (
    CoverGbotypeClaims,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.cover_gbotype_documents import (
    CoverGbotypeDocuments,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.cover_gbotype_insurance_flows import (
    CoverGbotypeInsuranceFlows,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.cover_gbotype_premiums import (
    CoverGbotypePremiums,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.cover_gbotype_reinsurers import (
    CoverGbotypeReinsurers,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.cover_gbotype_risks import (
    CoverGbotypeRisks,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.cover_gbotype_vessels import (
    CoverGbotypeVessels,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.coverage_type import (
    ExposuresType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.coverages_type import (
    CoveragesType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.deductibles_type import (
    DeductiblesType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.deductions_type import (
    DeductionsType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.engineering_type import (
    EngineeringType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.extensions_type import (
    ExtensionsType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.fronting_involvement_type import (
    FrontingInvolvementType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.limits_type import (
    LimitsType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.policy_type_enum import (
    PolicyTypeEnum,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.policyholder_involvement import (
    PolicyholderInvolvement,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.total_deductions_type import (
    TotalDeductionsType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.total_premium_type import (
    TotalPremiumType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class CoverGbotype(AgreementType):
    class Meta:
        name = "CoverGBOType"

    declaration_number: None | Idtype = field(
        default=None,
        metadata={
            "name": "DeclarationNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    claim_jurisdiction: None | TextType = field(
        default=None,
        metadata={
            "name": "ClaimJurisdiction",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    cost_in_addition: bool = field(
        default=False,
        metadata={
            "name": "CostInAddition",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    policy_jurisdiction: None | TextType = field(
        default=None,
        metadata={
            "name": "PolicyJurisdiction",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    layer: None | NumberType = field(
        default=None,
        metadata={
            "name": "Layer",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    share: None | PercentType = field(
        default=None,
        metadata={
            "name": "Share",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    visible: None | bool = field(
        default=None,
        metadata={
            "name": "Visible",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    country_of_business: None | str = field(
        default=None,
        metadata={
            "name": "CountryOfBusiness",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "pattern": r"[A-Z][A-Z]",
        },
    )
    cedants: None | CoverGbotypeCedants = field(
        default=None,
        metadata={
            "name": "Cedants",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    front: None | FrontingInvolvementType = field(
        default=None,
        metadata={
            "name": "Front",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    reinsurers: None | CoverGbotypeReinsurers = field(
        default=None,
        metadata={
            "name": "Reinsurers",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    insurance_flows: None | CoverGbotypeInsuranceFlows = field(
        default=None,
        metadata={
            "name": "InsuranceFlows",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    risks: None | CoverGbotypeRisks = field(
        default=None,
        metadata={
            "name": "Risks",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    vessels: None | CoverGbotypeVessels = field(
        default=None,
        metadata={
            "name": "Vessels",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    policy_type: None | PolicyTypeEnum = field(
        default=None,
        metadata={
            "name": "PolicyType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    coverages: None | CoveragesType = field(
        default=None,
        metadata={
            "name": "Coverages",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    policy_holder_involvement: None | PolicyholderInvolvement = field(
        default=None,
        metadata={
            "name": "PolicyHolderInvolvement",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    deductibles: None | DeductiblesType = field(
        default=None,
        metadata={
            "name": "Deductibles",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    deductions: None | DeductionsType = field(
        default=None,
        metadata={
            "name": "Deductions",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    total_deductions: None | TotalDeductionsType = field(
        default=None,
        metadata={
            "name": "TotalDeductions",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    extensions: None | ExtensionsType = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    limits: None | LimitsType = field(
        default=None,
        metadata={
            "name": "Limits",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    exposures: None | ExposuresType = field(
        default=None,
        metadata={
            "name": "Exposures",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    premiums: None | CoverGbotypePremiums = field(
        default=None,
        metadata={
            "name": "Premiums",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    total_premium: None | TotalPremiumType = field(
        default=None,
        metadata={
            "name": "TotalPremium",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    clauses: None | ClausesType = field(
        default=None,
        metadata={
            "name": "Clauses",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    exchange_rate: None | NumericType = field(
        default=None,
        metadata={
            "name": "ExchangeRate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    is_centralised_premium_payment: None | bool = field(
        default=None,
        metadata={
            "name": "IsCentralisedPremiumPayment",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    instruct_date: None | DateTimeType = field(
        default=None,
        metadata={
            "name": "InstructDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    date_sent_to_broker: None | DateTimeType = field(
        default=None,
        metadata={
            "name": "DateSentToBroker",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    date_policy_issued: None | DateTimeType = field(
        default=None,
        metadata={
            "name": "DatePolicyIssued",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    payment_date: None | DateTimeType = field(
        default=None,
        metadata={
            "name": "PaymentDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    documents: None | CoverGbotypeDocuments = field(
        default=None,
        metadata={
            "name": "Documents",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    country_of_risk: None | str = field(
        default=None,
        metadata={
            "name": "CountryOfRisk",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
            "pattern": r"[A-Z][A-Z]",
        },
    )
    claims: None | CoverGbotypeClaims = field(
        default=None,
        metadata={
            "name": "Claims",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    engineering: None | EngineeringType = field(
        default=None,
        metadata={
            "name": "Engineering",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
