from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.event_selector_type import EventSelectorType
from sdmx_ml.models.notification_urltype import NotificationUrltype
from sdmx_ml.models.validity_period_type import ValidityPeriodType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class SubscriptionType:
    """
    SubscriptionType describes the details of a subscription to a
    registration or change event for registry resources.

    When it occurs as the content of a response message, the registry URN
    must be provide, unless the response is a failure notification for the
    creation of a new subscription.

    :ivar organisation: Organisation provides a reference to the
        organisation that owns this subscription. The reference is
        provided via a URN and/or a complete set of reference fields.
    :ivar registry_urn: RegistryURN is used to identify the subscription
        in the case of deletion or modification. This should be provided
        in all response messages, unless the response it a notification
        of the failure to create a newly submitted subscription - in
        which case there will be no registry assigned URN.
    :ivar notification_mail_to: NotificationMailTo holds an e-mail
        address (the "mailto:" protocol). Multiple email address can be
        notified for a single subscription.
    :ivar notification_http: NotificationHTTP holds an http address to
        which notifications can be addressed as POSTs. Multiple http
        address may be notified for a single subscription event.
    :ivar subscriber_assigned_id: SubscriberAssignedID allows the
        subscriber to specify an identification which will be returned
        as part of the notification for the subscribed events. This
        should be used if multiple new requests are made, so that the
        responses can be accurately correlated to the requests.
    :ivar validity_period: Validity period sets a start and end date for
        the subscription.
    :ivar event_selector: EventSelector indicates an event or events for
        the subscription.
    """

    organisation: str | None = field(
        default=None,
        metadata={
            "name": "Organisation",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "required": True,
            "pattern": r".+\.base\.Agency=.+:AGENCIES\(.+\).+|.+\.base\.DataConsumer=.+:DATA_CONSUMERS\(.+\).+|.+\.base\.DataProvider=.+:DATA_PROVIDERS\(.+\).+|.+\.base\.MetadataProvider=.+:METADATA_PROVIDERS\(.+\).+|.+\.base\.OrganisationUnit=.+",
        },
    )
    registry_urn: str | None = field(
        default=None,
        metadata={
            "name": "RegistryURN",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
        },
    )
    notification_mail_to: tuple[NotificationUrltype, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "NotificationMailTo",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
        },
    )
    notification_http: tuple[NotificationUrltype, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "NotificationHTTP",
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
    validity_period: ValidityPeriodType | None = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "required": True,
        },
    )
    event_selector: EventSelectorType | None = field(
        default=None,
        metadata={
            "name": "EventSelector",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "required": True,
        },
    )
