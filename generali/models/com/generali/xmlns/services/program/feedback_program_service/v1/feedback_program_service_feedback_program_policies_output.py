from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.feedback_program_policies_response import FeedbackProgramPoliciesResponse

__NAMESPACE__ = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"


@dataclass
class FeedbackProgramServiceFeedbackProgramPoliciesOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["FeedbackProgramServiceFeedbackProgramPoliciesOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        feedback_program_policies_response: Optional[FeedbackProgramPoliciesResponse] = field(
            default=None,
            metadata={
                "name": "FeedbackProgramPoliciesResponse",
                "type": "Element",
                "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            }
        )
        fault: Optional["FeedbackProgramServiceFeedbackProgramPoliciesOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
