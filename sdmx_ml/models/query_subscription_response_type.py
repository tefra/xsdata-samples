from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.status_message_type_2 import StatusMessageType2
from sdmx_ml.models.subscription_type import SubscriptionType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class QuerySubscriptionResponseType:
    """QuerySubscriptionResponseType describes the structure of a subscription
    query response.

    A status will describe the success or failure of the request (and
    provide error or warning messages if necessary). If the query was
    successful, details of all of the organisation's subscriptions will
    be provided.

    :ivar status_message: StatusMessage provides that status for the
        query subscription request, and if necessary, any error or
        warning information.
    :ivar subscription: Subscription contains the details of a
        subscription for the organisation. This may occur multiple times
        for each subscription.
    """

    status_message: Optional[StatusMessageType2] = field(
        default=None,
        metadata={
            "name": "StatusMessage",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "required": True,
        },
    )
    subscription: tuple[SubscriptionType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Subscription",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
        },
    )
