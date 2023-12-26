from dataclasses import dataclass
from .terminate_subscription_request_structure import (
    TerminateSubscriptionRequestStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TerminateSubscriptionRequest(TerminateSubscriptionRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
