from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.party_ids import PartyIds
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.reinsurance_agreements import ReinsuranceAgreements
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.risks import Risks

__NAMESPACE__ = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"


@dataclass
class LocalPolicy:
    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    local_policy_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalPolicyID",
            "type": "Element",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
        }
    )
    party_ids: Optional[PartyIds] = field(
        default=None,
        metadata={
            "name": "PartyIDs",
            "type": "Element",
        }
    )
    risks: Optional[Risks] = field(
        default=None,
        metadata={
            "name": "Risks",
            "type": "Element",
        }
    )
    reinsurance_agreements: Optional[ReinsuranceAgreements] = field(
        default=None,
        metadata={
            "name": "ReinsuranceAgreements",
            "type": "Element",
        }
    )
    inception_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "InceptionDate",
            "type": "Element",
        }
    )
    issuance_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "IssuanceDate",
            "type": "Element",
        }
    )
    expiry_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpiryDate",
            "type": "Element",
        }
    )
