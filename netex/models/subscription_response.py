from dataclasses import dataclass
from netex.models.subscription_response_structure import SubscriptionResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SubscriptionResponse(SubscriptionResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
