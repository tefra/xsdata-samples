from __future__ import annotations

from dataclasses import dataclass

from .abstract_subscription_structure import AbstractSubscriptionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractFunctionalServiceSubscriptionRequest(
    AbstractSubscriptionStructure
):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
