from __future__ import annotations

from dataclasses import dataclass

from .subscription_response_structure import SubscriptionResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SubscriptionResponse(SubscriptionResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
