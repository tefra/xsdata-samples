from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbs/enterprise/organisation/v1"


@dataclass(kw_only=True)
class FeedbackProgramServiceFeedbackProgramPoliciesOutputBodyFault:
    class Meta:
        global_type = False

    faultcode: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultstring: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultactor: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    detail: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
