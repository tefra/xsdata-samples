from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass
class ReinsuranceAgreements:
    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    reinsurance_agreement_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReinsuranceAgreementID",
            "type": "Element",
            "required": True,
        },
    )
