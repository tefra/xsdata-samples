from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.idtype import Idtype
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import TextType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.agreement_type import AgreementType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.cedant_involvement_type import CedantInvolvementType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.claim_type import ClaimType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.clauses_type import ClausesType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.coverage_type import ExposuresType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.coverages_type import CoveragesType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.deductibles_type import DeductiblesType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.deductions_type import DeductionsType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.engineering_type import EngineeringType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.extensions_type import ExtensionsType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.fronting_involvement_type import FrontingInvolvementType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.insurance_flow_type import InsuranceFlowType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.limits_type import LimitsType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.policy_type_enum import PolicyTypeEnum
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.policyholder_involvement import PolicyholderInvolvement
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.premium_type import PremiumType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.reinsurer_involvement_type import ReinsurerInvolvementType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.risk_type import RiskType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.total_deductions_type import TotalDeductionsType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.total_premium_type import TotalPremiumType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.vessel_type import VesselType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.document_type import DocumentType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


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
        }
    )
    claim_jurisdiction: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "ClaimJurisdiction",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    cost_in_addition: bool = field(
        default=False,
        metadata={
            "name": "CostInAddition",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    policy_jurisdiction: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "PolicyJurisdiction",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    layer: Optional[int] = field(
        default=None,
        metadata={
            "name": "Layer",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    share: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Share",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Visible",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    country_of_business: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryOfBusiness",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "pattern": r"[A-Z][A-Z]",
        }
    )
    cedants: Optional["CoverGbotype.Cedants"] = field(
        default=None,
        metadata={
            "name": "Cedants",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    front: Optional[FrontingInvolvementType] = field(
        default=None,
        metadata={
            "name": "Front",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    reinsurers: Optional["CoverGbotype.Reinsurers"] = field(
        default=None,
        metadata={
            "name": "Reinsurers",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    insurance_flows: Optional["CoverGbotype.InsuranceFlows"] = field(
        default=None,
        metadata={
            "name": "InsuranceFlows",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    risks: Optional["CoverGbotype.Risks"] = field(
        default=None,
        metadata={
            "name": "Risks",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    vessels: Optional["CoverGbotype.Vessels"] = field(
        default=None,
        metadata={
            "name": "Vessels",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    policy_type: Optional[PolicyTypeEnum] = field(
        default=None,
        metadata={
            "name": "PolicyType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    coverages: Optional[CoveragesType] = field(
        default=None,
        metadata={
            "name": "Coverages",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    policy_holder_involvement: Optional[PolicyholderInvolvement] = field(
        default=None,
        metadata={
            "name": "PolicyHolderInvolvement",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
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
    deductions: Optional[DeductionsType] = field(
        default=None,
        metadata={
            "name": "Deductions",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    total_deductions: Optional[TotalDeductionsType] = field(
        default=None,
        metadata={
            "name": "TotalDeductions",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    extensions: Optional[ExtensionsType] = field(
        default=None,
        metadata={
            "name": "Extensions",
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
    exposures: Optional[ExposuresType] = field(
        default=None,
        metadata={
            "name": "Exposures",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    premiums: Optional["CoverGbotype.Premiums"] = field(
        default=None,
        metadata={
            "name": "Premiums",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
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
    clauses: Optional[ClausesType] = field(
        default=None,
        metadata={
            "name": "Clauses",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    exchange_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ExchangeRate",
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
    instruct_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "InstructDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    date_sent_to_broker: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DateSentToBroker",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    date_policy_issued: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DatePolicyIssued",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    payment_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "PaymentDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    documents: Optional["CoverGbotype.Documents"] = field(
        default=None,
        metadata={
            "name": "Documents",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    country_of_risk: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryOfRisk",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
            "pattern": r"[A-Z][A-Z]",
        }
    )
    claims: Optional["CoverGbotype.Claims"] = field(
        default=None,
        metadata={
            "name": "Claims",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    engineering: Optional[EngineeringType] = field(
        default=None,
        metadata={
            "name": "Engineering",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )

    @dataclass
    class Cedants:
        cedant: List[CedantInvolvementType] = field(
            default_factory=list,
            metadata={
                "name": "Cedant",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            }
        )

    @dataclass
    class Reinsurers:
        reinsurer: List[ReinsurerInvolvementType] = field(
            default_factory=list,
            metadata={
                "name": "Reinsurer",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
                "min_occurs": 1,
            }
        )

    @dataclass
    class InsuranceFlows:
        insurance_flow: List[InsuranceFlowType] = field(
            default_factory=list,
            metadata={
                "name": "InsuranceFlow",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Risks:
        risk: List[RiskType] = field(
            default_factory=list,
            metadata={
                "name": "Risk",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            }
        )

    @dataclass
    class Vessels:
        vessel: List[VesselType] = field(
            default_factory=list,
            metadata={
                "name": "Vessel",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            }
        )

    @dataclass
    class Premiums:
        premium: List[PremiumType] = field(
            default_factory=list,
            metadata={
                "name": "Premium",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            }
        )

    @dataclass
    class Documents:
        document: List[DocumentType] = field(
            default_factory=list,
            metadata={
                "name": "Document",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            }
        )

    @dataclass
    class Claims:
        claim: List[ClaimType] = field(
            default_factory=list,
            metadata={
                "name": "Claim",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            }
        )
