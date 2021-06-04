from dataclasses import dataclass
from netex.models.abstract_subscription_structure import AbstractSubscriptionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractFunctionalServiceSubscriptionRequest(AbstractSubscriptionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
