from dataclasses import dataclass
from netex.models.terminate_subscription_response_structure import TerminateSubscriptionResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TerminateSubscriptionResponse(TerminateSubscriptionResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
