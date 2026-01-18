from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.local_policies_type_local_policy_party_ids_party_id import (
    LocalPoliciesTypeLocalPolicyPartyIdsPartyId,
)

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass(kw_only=True)
class LocalPoliciesTypeLocalPolicyPartyIds:
    class Meta:
        global_type = False

    party_id: list[LocalPoliciesTypeLocalPolicyPartyIdsPartyId] = field(
        default_factory=list,
        metadata={
            "name": "PartyID",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            "min_occurs": 1,
        },
    )
