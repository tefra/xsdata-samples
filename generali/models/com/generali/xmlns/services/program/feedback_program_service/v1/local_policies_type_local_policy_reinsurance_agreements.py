from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass
class LocalPoliciesTypeLocalPolicyReinsuranceAgreements:
    class Meta:
        global_type = False

    reinsurance_agreement_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ReinsuranceAgreementID",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            "min_occurs": 1,
        },
    )
