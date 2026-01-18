from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass
class FeedbackProgramPoliciesResponse:
    """
    :ivar response_code:
    :ivar response_text:
    :ivar request_id: If the request was successfully queued, a
        RequestID will be returned.
    """

    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    response_code: None | str = field(
        default=None,
        metadata={
            "name": "ResponseCode",
            "type": "Element",
            "required": True,
        },
    )
    response_text: None | str = field(
        default=None,
        metadata={
            "name": "ResponseText",
            "type": "Element",
        },
    )
    request_id: None | str = field(
        default=None,
        metadata={
            "name": "RequestID",
            "type": "Element",
        },
    )
