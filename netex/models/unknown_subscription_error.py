from dataclasses import dataclass
from .unknown_subscription_error_structure import UnknownSubscriptionErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnknownSubscriptionError(UnknownSubscriptionErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
