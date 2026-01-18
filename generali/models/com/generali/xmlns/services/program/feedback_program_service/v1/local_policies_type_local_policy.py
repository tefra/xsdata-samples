from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.local_policies_type_local_policy_party_ids import (
    LocalPoliciesTypeLocalPolicyPartyIds,
)
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.local_policies_type_local_policy_reinsurance_agreements import (
    LocalPoliciesTypeLocalPolicyReinsuranceAgreements,
)
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.local_policies_type_local_policy_risks import (
    LocalPoliciesTypeLocalPolicyRisks,
)
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.status import (
    Status,
)

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass
class LocalPoliciesTypeLocalPolicy:
    """
    :ivar local_policy_id: Reference(s) used in the local system to
        represent this policy.
    :ivar local_policy_reference: Reference(s) used in the local system
        to represent this policy, before a Policy ID is generated
        (introduced due to ESP requirement)
    :ivar producing_office_ref: This would be the Producing office
        Policy reference
    :ivar reinsurance_policy_ref: This would be the Reinsurance Policy
        Reference used by Clearing house countries
    :ivar status:
    :ivar party_ids:
    :ivar risks:
    :ivar reinsurance_agreements:
    :ivar inception_date:
    :ivar issuance_date:
    :ivar expiry_date:
    """

    class Meta:
        global_type = False

    local_policy_id: str | None = field(
        default=None,
        metadata={
            "name": "LocalPolicyID",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
        },
    )
    local_policy_reference: str | None = field(
        default=None,
        metadata={
            "name": "LocalPolicyReference",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
        },
    )
    producing_office_ref: str | None = field(
        default=None,
        metadata={
            "name": "ProducingOfficeRef",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
        },
    )
    reinsurance_policy_ref: str | None = field(
        default=None,
        metadata={
            "name": "ReinsurancePolicyRef",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
        },
    )
    status: Status | None = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            "required": True,
        },
    )
    party_ids: LocalPoliciesTypeLocalPolicyPartyIds | None = field(
        default=None,
        metadata={
            "name": "PartyIDs",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
        },
    )
    risks: LocalPoliciesTypeLocalPolicyRisks | None = field(
        default=None,
        metadata={
            "name": "Risks",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
        },
    )
    reinsurance_agreements: (
        LocalPoliciesTypeLocalPolicyReinsuranceAgreements | None
    ) = field(
        default=None,
        metadata={
            "name": "ReinsuranceAgreements",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
        },
    )
    inception_date: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "InceptionDate",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            "nillable": True,
        },
    )
    issuance_date: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "IssuanceDate",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            "nillable": True,
        },
    )
    expiry_date: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "ExpiryDate",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            "nillable": True,
        },
    )
