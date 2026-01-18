from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.action_type import ActionType
from sdmx_ml.models.subscription_type import SubscriptionType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class SubscriptionRequestType:
    """
    SubscriptionRequestType describes the structure of a single
    subscription request.

    It contains subscription details and an action field to indicate the
    action to be taken on the contained subscription. Note that if the
    action is update or delete, then the registry supplied URN for the
    subscription must be included.

    :ivar subscription: Subscription contains the details of the
        subscription to be added, updated, or deleted.
    :ivar action: The action attribute indicates whether this is an
        addition, a modification, or a deletion of a subscription.
    """

    subscription: None | SubscriptionType = field(
        default=None,
        metadata={
            "name": "Subscription",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "required": True,
        },
    )
    action: None | ActionType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
