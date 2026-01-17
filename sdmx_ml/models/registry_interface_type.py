from dataclasses import dataclass, field
from typing import Optional, Union

from sdmx_ml.models.basic_header_type import BasicHeaderType
from sdmx_ml.models.footer import Footer
from sdmx_ml.models.notify_registry_event_type import NotifyRegistryEventType
from sdmx_ml.models.query_registration_request_type import (
    QueryRegistrationRequestType,
)
from sdmx_ml.models.query_registration_response_type import (
    QueryRegistrationResponseType,
)
from sdmx_ml.models.query_subscription_request_type import (
    QuerySubscriptionRequestType,
)
from sdmx_ml.models.query_subscription_response_type import (
    QuerySubscriptionResponseType,
)
from sdmx_ml.models.submit_registrations_request_type import (
    SubmitRegistrationsRequestType,
)
from sdmx_ml.models.submit_registrations_response_type import (
    SubmitRegistrationsResponseType,
)
from sdmx_ml.models.submit_structure_request_type_1 import (
    SubmitStructureRequestType1,
)
from sdmx_ml.models.submit_structure_response_type_1 import (
    SubmitStructureResponseType1,
)
from sdmx_ml.models.submit_subscriptions_request_type import (
    SubmitSubscriptionsRequestType,
)
from sdmx_ml.models.submit_subscriptions_response_type import (
    SubmitSubscriptionsResponseType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"


@dataclass(frozen=True)
class RegistryInterfaceType:
    """
    This is a type which describes a structure for holding all of the
    various dedicated registry interface message types.
    """

    header: Optional[BasicHeaderType] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
            "required": True,
        },
    )
    choice: Optional[
        Union[
            SubmitRegistrationsRequestType,
            SubmitRegistrationsResponseType,
            QueryRegistrationRequestType,
            QueryRegistrationResponseType,
            SubmitStructureRequestType1,
            SubmitStructureResponseType1,
            SubmitSubscriptionsRequestType,
            SubmitSubscriptionsResponseType,
            QuerySubscriptionRequestType,
            QuerySubscriptionResponseType,
            NotifyRegistryEventType,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SubmitRegistrationsRequest",
                    "type": SubmitRegistrationsRequestType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
                },
                {
                    "name": "SubmitRegistrationsResponse",
                    "type": SubmitRegistrationsResponseType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
                },
                {
                    "name": "QueryRegistrationRequest",
                    "type": QueryRegistrationRequestType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
                },
                {
                    "name": "QueryRegistrationResponse",
                    "type": QueryRegistrationResponseType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
                },
                {
                    "name": "SubmitStructureRequest",
                    "type": SubmitStructureRequestType1,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
                },
                {
                    "name": "SubmitStructureResponse",
                    "type": SubmitStructureResponseType1,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
                },
                {
                    "name": "SubmitSubscriptionsRequest",
                    "type": SubmitSubscriptionsRequestType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
                },
                {
                    "name": "SubmitSubscriptionsResponse",
                    "type": SubmitSubscriptionsResponseType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
                },
                {
                    "name": "QuerySubscriptionRequest",
                    "type": QuerySubscriptionRequestType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
                },
                {
                    "name": "QuerySubscriptionResponse",
                    "type": QuerySubscriptionResponseType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
                },
                {
                    "name": "NotifyRegistryEvent",
                    "type": NotifyRegistryEventType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
                },
            ),
        },
    )
    footer: Optional[Footer] = field(
        default=None,
        metadata={
            "name": "Footer",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message/footer",
        },
    )
