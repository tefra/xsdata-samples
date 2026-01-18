from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass(kw_only=True)
class ReinsuranceAgreements:
    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    reinsurance_agreement_id: str = field(
        metadata={
            "name": "ReinsuranceAgreementID",
            "type": "Element",
            "required": True,
        }
    )
