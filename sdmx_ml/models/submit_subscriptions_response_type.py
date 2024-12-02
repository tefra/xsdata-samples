from dataclasses import dataclass, field

from sdmx_ml.models.subscription_status_type import SubscriptionStatusType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class SubmitSubscriptionsResponseType:
    """SubmitSubscriptionsResponseType describes the structure of the response to a
    new subscription submission.

    A status is provided for each subscription in the request.

    :ivar subscription_status: SubscriptionStatus contains information
        which describes the success or failure of a subscription
        request, providing any error messages in the event of failure.
        The statuses should occur in the same order as the requests when
        responding to a message with multiple subscription requests. If
        a subscriber-assigned identification for the subscription is
        provided, it will be returned to allow for accurate matching of
        the responses to the requests. A registry assigned URN will be
        returned for any successfully created, updated, or deleted
        subscription.
    """

    subscription_status: tuple[SubscriptionStatusType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SubscriptionStatus",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "min_occurs": 1,
        },
    )
