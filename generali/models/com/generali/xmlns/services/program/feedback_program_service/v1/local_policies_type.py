from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.risk_type import RiskType
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.status_value import StatusValue

__NAMESPACE__ = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"


@dataclass
class LocalPoliciesType:
    local_policy: List["LocalPoliciesType.LocalPolicy"] = field(
        default_factory=list,
        metadata={
            "name": "LocalPolicy",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
        }
    )

    @dataclass
    class LocalPolicy:
        """
        :ivar local_policy_id: Reference(s) used in the local system to
            represent this policy.
        :ivar local_policy_reference: Reference(s) used in the local
            system to represent this policy, before a Policy ID is
            generated (introduced due to ESP requirement)
        :ivar producing_office_ref: This would be the Producing office
            Policy reference
        :ivar reinsurance_policy_ref: This would be the Reinsurance
            Policy Reference used by Clearing house countries
        :ivar status:
        :ivar party_ids:
        :ivar risks:
        :ivar reinsurance_agreements:
        :ivar inception_date:
        :ivar issuance_date:
        :ivar expiry_date:
        """
        local_policy_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "LocalPolicyID",
                "type": "Element",
                "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            }
        )
        local_policy_reference: Optional[str] = field(
            default=None,
            metadata={
                "name": "LocalPolicyReference",
                "type": "Element",
                "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            }
        )
        producing_office_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "ProducingOfficeRef",
                "type": "Element",
                "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            }
        )
        reinsurance_policy_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "ReinsurancePolicyRef",
                "type": "Element",
                "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            }
        )
        status: Optional[StatusValue] = field(
            default=None,
            metadata={
                "name": "Status",
                "type": "Element",
                "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
                "required": True,
            }
        )
        party_ids: Optional["LocalPoliciesType.LocalPolicy.PartyIds"] = field(
            default=None,
            metadata={
                "name": "PartyIDs",
                "type": "Element",
                "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            }
        )
        risks: Optional["LocalPoliciesType.LocalPolicy.Risks"] = field(
            default=None,
            metadata={
                "name": "Risks",
                "type": "Element",
                "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            }
        )
        reinsurance_agreements: Optional["LocalPoliciesType.LocalPolicy.ReinsuranceAgreements"] = field(
            default=None,
            metadata={
                "name": "ReinsuranceAgreements",
                "type": "Element",
                "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            }
        )
        inception_date: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "InceptionDate",
                "type": "Element",
                "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
                "nillable": True,
            }
        )
        issuance_date: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "IssuanceDate",
                "type": "Element",
                "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
                "nillable": True,
            }
        )
        expiry_date: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "ExpiryDate",
                "type": "Element",
                "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
                "nillable": True,
            }
        )

        @dataclass
        class PartyIds:
            party_id: List["LocalPoliciesType.LocalPolicy.PartyIds.PartyId"] = field(
                default_factory=list,
                metadata={
                    "name": "PartyID",
                    "type": "Element",
                    "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
                    "min_occurs": 1,
                }
            )

            @dataclass
            class PartyId:
                """
                :ivar value:
                :ivar party_type: Party type will be one of the
                    following: INS - Insured CED - Cedant REI -
                    Reinsurer BRK - Broker INC - Insurer
                :ivar party_guns:
                """
                value: str = field(
                    default="",
                    metadata={
                        "required": True,
                    }
                )
                party_type: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "PartyType",
                        "type": "Attribute",
                    }
                )
                party_guns: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "PartyGUNS",
                        "type": "Attribute",
                        "required": True,
                    }
                )

        @dataclass
        class Risks:
            risk: List[RiskType] = field(
                default_factory=list,
                metadata={
                    "name": "Risk",
                    "type": "Element",
                    "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
                }
            )

        @dataclass
        class ReinsuranceAgreements:
            reinsurance_agreement_id: List[str] = field(
                default_factory=list,
                metadata={
                    "name": "ReinsuranceAgreementID",
                    "type": "Element",
                    "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
                    "min_occurs": 1,
                }
            )
