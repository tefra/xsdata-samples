from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass(kw_only=True)
class LocalPoliciesTypeLocalPolicyReinsuranceAgreements:
    class Meta:
        global_type = False

    reinsurance_agreement_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ReinsuranceAgreementID",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            "min_occurs": 1,
        },
    )
