from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.amount_type import AmountType
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import TextType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.sic_classification_type import SicClassificationType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.agreement_type import AgreementType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.cyber_exclusion_type import CyberExclusionType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.deductibles_type import DeductiblesType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.legal_cost_type import LegalCostType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.limits_type import LimitsType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.perils_structure_type import PerilsStructureType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.pricing_type import PricingType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.producer_involvement_type import ProducerInvolvementType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.program_gbotype_covers import ProgramGbotypeCovers
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.program_gbotype_documents import ProgramGbotypeDocuments
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.program_gbotype_premium_factors import ProgramGbotypePremiumFactors
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.program_gbotype_risks import ProgramGbotypeRisks
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.total_premium_type import TotalPremiumType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


@dataclass
class ProgramGbotype(AgreementType):
    class Meta:
        name = "ProgramGBOType"

    long_term_agreement: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LongTermAgreement",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    long_term_start_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LongTermStartDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    long_term_end_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LongTermEndDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    on_risk_since: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OnRiskSince",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    renewal_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RenewalDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    year_sequence_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "YearSequenceNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    producer: Optional[ProducerInvolvementType] = field(
        default=None,
        metadata={
            "name": "Producer",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    cancellation_days_notice: Optional[int] = field(
        default=None,
        metadata={
            "name": "CancellationDaysNotice",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    risks: Optional[ProgramGbotypeRisks] = field(
        default=None,
        metadata={
            "name": "Risks",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    covers: Optional[ProgramGbotypeCovers] = field(
        default=None,
        metadata={
            "name": "Covers",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    deductibles: Optional[DeductiblesType] = field(
        default=None,
        metadata={
            "name": "Deductibles",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    limits: Optional[LimitsType] = field(
        default=None,
        metadata={
            "name": "Limits",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    premium_factors: Optional[ProgramGbotypePremiumFactors] = field(
        default=None,
        metadata={
            "name": "PremiumFactors",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    perils: Optional[PerilsStructureType] = field(
        default=None,
        metadata={
            "name": "Perils",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    si_ccode: Optional[SicClassificationType] = field(
        default=None,
        metadata={
            "name": "SiCCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    legal_cost: Optional[LegalCostType] = field(
        default=None,
        metadata={
            "name": "LegalCost",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    total_premium: Optional[TotalPremiumType] = field(
        default=None,
        metadata={
            "name": "TotalPremium",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    program_limit_of_indemnity: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "ProgramLimitOfIndemnity",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    pharmaceutical_risk: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PharmaceuticalRisk",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    is_centralised_premium_payment: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsCentralisedPremiumPayment",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    to_portal_indicator: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "ToPortalIndicator",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    documents: Optional[ProgramGbotypeDocuments] = field(
        default=None,
        metadata={
            "name": "Documents",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    mprindicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MPRIndicator",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    sanction_and_compliance_flag: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SanctionAndComplianceFlag",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    pricing: Optional[PricingType] = field(
        default=None,
        metadata={
            "name": "Pricing",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    cyber_exclusion: Optional[CyberExclusionType] = field(
        default=None,
        metadata={
            "name": "CyberExclusion",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    family_submission_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "FamilySubmissionReference",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    car_submission_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "CarSubmissionReference",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    project_type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProjectTypeCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    publish_claims_with_paid_values: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PublishClaimsWithPaidValues",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    publish_claims_without_paid_values: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PublishClaimsWithoutPaidValues",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
