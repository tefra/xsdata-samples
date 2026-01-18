from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

from xsdata.models.datatype import XmlDateTime

from sdmx_ml.models.action_type import ActionType
from sdmx_ml.models.registration_event_type import RegistrationEventType
from sdmx_ml.models.structural_event_type import StructuralEventType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class NotifyRegistryEventType:
    """
    NotifyRegistryEventType describes the structure a registry
    notification, in response to a subscription to a registry event.

    At a minimum, the event time, a reference to the change object, a
    reference to the underlying subscription triggering the notification,
    and the action that took place on the object are sent. In addition, the
    full details of the object may be provided at the discretion of the
    registry. In the event that the details are not sent, it will be
    possible to query for the details of the changed object using the
    reference provided.

    :ivar event_time: EventTime specifies the time of the triggering
        event.
    :ivar object_urn_or_registration_id:
    :ivar subscription_urn: SubscriptionURN provides the
        registry/repository URN of the subscription that is the cause of
        this notification being sent.
    :ivar event_action: EventAction indicates the nature of the event -
        whether the action was an addition, a modification, or a
        deletion.
    :ivar structural_event_or_registration_event:
    """

    event_time: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "EventTime",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "required": True,
        },
    )
    object_urn_or_registration_id: NotifyRegistryEventType.ObjectUrn | NotifyRegistryEventType.RegistrationId | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ObjectURN",
                    "type": ForwardRef("NotifyRegistryEventType.ObjectUrn"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "RegistrationID",
                    "type": ForwardRef(
                        "NotifyRegistryEventType.RegistrationId"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
            ),
        },
    )
    subscription_urn: str | None = field(
        default=None,
        metadata={
            "name": "SubscriptionURN",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "required": True,
        },
    )
    event_action: ActionType | None = field(
        default=None,
        metadata={
            "name": "EventAction",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "required": True,
        },
    )
    structural_event_or_registration_event: StructuralEventType | RegistrationEventType | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StructuralEvent",
                    "type": StructuralEventType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "RegistrationEvent",
                    "type": RegistrationEventType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
            ),
        },
    )

    @dataclass(frozen=True)
    class ObjectUrn:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass(frozen=True)
    class RegistrationId:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r"[A-Za-z0-9_@$\-]+",
            },
        )
