from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.status_message_type_2 import StatusMessageType2

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class SubscriptionStatusType:
    """
    SubscriptionStatusType describes the structure a status for a single
    subscription request.

    :ivar subscription_urn: SubscriptionURN contains the registry
        generated URN for the subscription, and will be returned for any
        successfully created, updated, or deleted subscription.
    :ivar subscriber_assigned_id: SubscriberAssignedID is the id
        assigned by the subscriber to the subscription. If it existed in
        the subscription request, it will be returned.
    :ivar status_message: StatusMessage provides that status for the
        subscription request, and if necessary, any error or warning
        information.
    """

    subscription_urn: str | None = field(
        default=None,
        metadata={
            "name": "SubscriptionURN",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
        },
    )
    subscriber_assigned_id: str | None = field(
        default=None,
        metadata={
            "name": "SubscriberAssignedID",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
    status_message: StatusMessageType2 | None = field(
        default=None,
        metadata={
            "name": "StatusMessage",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "required": True,
        },
    )
