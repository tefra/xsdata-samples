from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CapabilityGeneralInteractionStructure:
    interaction: CapabilityGeneralInteractionStructure.Interaction | None = field(
        default=None,
        metadata={
            "name": "Interaction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    delivery: CapabilityGeneralInteractionStructure.Delivery | None = (
        field(
            default=None,
            metadata={
                "name": "Delivery",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
    )
    multipart_despatch: bool = field(
        default=True,
        metadata={
            "name": "MultipartDespatch",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    multiple_subscriber_filter: bool = field(
        default=False,
        metadata={
            "name": "MultipleSubscriberFilter",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    has_confirm_delivery: bool = field(
        default=False,
        metadata={
            "name": "HasConfirmDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    has_heartbeat: bool = field(
        default=False,
        metadata={
            "name": "HasHeartbeat",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    visit_numberis_order: bool | None = field(
        default=None,
        metadata={
            "name": "VisitNumberisOrder",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class Interaction:
        request_response: bool = field(
            default=True,
            metadata={
                "name": "RequestResponse",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
        publish_subscribe: bool = field(
            default=True,
            metadata={
                "name": "PublishSubscribe",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )

    @dataclass
    class Delivery:
        direct_delivery: bool | None = field(
            default=None,
            metadata={
                "name": "DirectDelivery",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
        fetched_delivery: bool | None = field(
            default=None,
            metadata={
                "name": "FetchedDelivery",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
