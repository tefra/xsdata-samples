from dataclasses import dataclass, field
from typing import Optional
from netex.models.request_structure import RequestStructure
from netex.models.subscription_context_structure import SubscriptionContextStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractSubscriptionRequestStructure(RequestStructure):
    consumer_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConsumerAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    subscription_filter_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriptionFilterIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    subscription_context: Optional[SubscriptionContextStructure] = field(
        default=None,
        metadata={
            "name": "SubscriptionContext",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
