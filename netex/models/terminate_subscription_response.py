from __future__ import annotations

from dataclasses import dataclass

from .terminate_subscription_response_structure import (
    TerminateSubscriptionResponseStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TerminateSubscriptionResponse(TerminateSubscriptionResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
