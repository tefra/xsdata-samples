from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass
class ReinsuranceAgreements:
    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    reinsurance_agreement_id: str | None = field(
        default=None,
        metadata={
            "name": "ReinsuranceAgreementID",
            "type": "Element",
            "required": True,
        },
    )
