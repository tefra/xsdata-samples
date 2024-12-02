from dataclasses import dataclass, field

from sdmx_ml.models.subscription_request_type import SubscriptionRequestType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class SubmitSubscriptionsRequestType:
    """SubmitSubscriptionsRequestType defines the payload of a request message used
    to submit addtions, updates, or deletions of subscriptions.

    Subscriptions are submitted to the registry to subscribe to
    registration and change events for specific registry resources.
    """

    subscription_request: tuple[SubscriptionRequestType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "min_occurs": 1,
        },
    )
