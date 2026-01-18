from __future__ import annotations

from dataclasses import dataclass, field

from .request_structure import RequestStructure
from .subscription_context_structure import SubscriptionContextStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractSubscriptionRequestStructure(RequestStructure):
    consumer_address: str | None = field(
        default=None,
        metadata={
            "name": "ConsumerAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_filter_identifier: str | None = field(
        default=None,
        metadata={
            "name": "SubscriptionFilterIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_context: SubscriptionContextStructure | None = field(
        default=None,
        metadata={
            "name": "SubscriptionContext",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
