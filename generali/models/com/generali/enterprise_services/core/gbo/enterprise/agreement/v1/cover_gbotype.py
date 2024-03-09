from dataclasses import dataclass, field
from typing import Optional

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

    declaration_number: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "DeclarationNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    claim_jurisdiction: Optional[TextType] = field(
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
    policy_jurisdiction: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "PolicyJurisdiction",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    layer: Optional[NumberType] = field(
        default=None,
        metadata={
            "name": "Layer",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    share: Optional[PercentType] = field(
        default=None,
        metadata={
            "name": "Share",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Visible",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    country_of_business: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryOfBusiness",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "pattern": r"[A-Z][A-Z]",
        },
    )
    cedants: Optional[CoverGbotypeCedants] = field(
        default=None,
        metadata={
            "name": "Cedants",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    front: Optional[FrontingInvolvementType] = field(
        default=None,
        metadata={
            "name": "Front",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    reinsurers: Optional[CoverGbotypeReinsurers] = field(
        default=None,
        metadata={
            "name": "Reinsurers",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    insurance_flows: Optional[CoverGbotypeInsuranceFlows] = field(
        default=None,
        metadata={
            "name": "InsuranceFlows",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    risks: Optional[CoverGbotypeRisks] = field(
        default=None,
        metadata={
            "name": "Risks",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    vessels: Optional[CoverGbotypeVessels] = field(
        default=None,
        metadata={
            "name": "Vessels",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    policy_type: Optional[PolicyTypeEnum] = field(
        default=None,
        metadata={
            "name": "PolicyType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    coverages: Optional[CoveragesType] = field(
        default=None,
        metadata={
            "name": "Coverages",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    policy_holder_involvement: Optional[PolicyholderInvolvement] = field(
        default=None,
        metadata={
            "name": "PolicyHolderInvolvement",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    deductibles: Optional[DeductiblesType] = field(
        default=None,
        metadata={
            "name": "Deductibles",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    deductions: Optional[DeductionsType] = field(
        default=None,
        metadata={
            "name": "Deductions",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    total_deductions: Optional[TotalDeductionsType] = field(
        default=None,
        metadata={
            "name": "TotalDeductions",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    extensions: Optional[ExtensionsType] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    limits: Optional[LimitsType] = field(
        default=None,
        metadata={
            "name": "Limits",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    exposures: Optional[ExposuresType] = field(
        default=None,
        metadata={
            "name": "Exposures",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    premiums: Optional[CoverGbotypePremiums] = field(
        default=None,
        metadata={
            "name": "Premiums",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    total_premium: Optional[TotalPremiumType] = field(
        default=None,
        metadata={
            "name": "TotalPremium",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    clauses: Optional[ClausesType] = field(
        default=None,
        metadata={
            "name": "Clauses",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    exchange_rate: Optional[NumericType] = field(
        default=None,
        metadata={
            "name": "ExchangeRate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    is_centralised_premium_payment: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsCentralisedPremiumPayment",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    instruct_date: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "InstructDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    date_sent_to_broker: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "DateSentToBroker",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    date_policy_issued: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "DatePolicyIssued",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    payment_date: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "PaymentDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    documents: Optional[CoverGbotypeDocuments] = field(
        default=None,
        metadata={
            "name": "Documents",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    country_of_risk: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryOfRisk",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
            "pattern": r"[A-Z][A-Z]",
        },
    )
    claims: Optional[CoverGbotypeClaims] = field(
        default=None,
        metadata={
            "name": "Claims",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    engineering: Optional[EngineeringType] = field(
        default=None,
        metadata={
            "name": "Engineering",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
