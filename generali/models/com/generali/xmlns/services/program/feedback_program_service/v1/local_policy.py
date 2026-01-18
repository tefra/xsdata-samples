from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.party_ids import (
    PartyIds,
)
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.reinsurance_agreements import (
    ReinsuranceAgreements,
)
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.risks import (
    Risks,
)

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass(kw_only=True)
class LocalPolicy:
    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    local_policy_id: str = field(
        metadata={
            "name": "LocalPolicyID",
            "type": "Element",
            "required": True,
        }
    )
    status: str = field(
        metadata={
            "name": "Status",
            "type": "Element",
            "required": True,
        }
    )
    party_ids: PartyIds = field(
        metadata={
            "name": "PartyIDs",
            "type": "Element",
            "required": True,
        }
    )
    risks: Risks = field(
        metadata={
            "name": "Risks",
            "type": "Element",
            "required": True,
        }
    )
    reinsurance_agreements: ReinsuranceAgreements = field(
        metadata={
            "name": "ReinsuranceAgreements",
            "type": "Element",
            "required": True,
        }
    )
    inception_date: XmlDateTime = field(
        metadata={
            "name": "InceptionDate",
            "type": "Element",
            "required": True,
        }
    )
    issuance_date: XmlDateTime = field(
        metadata={
            "name": "IssuanceDate",
            "type": "Element",
            "required": True,
        }
    )
    expiry_date: XmlDateTime = field(
        metadata={
            "name": "ExpiryDate",
            "type": "Element",
            "required": True,
        }
    )
