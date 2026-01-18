from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class CapabilityGeneralInteractionStructure:
    interaction: CapabilityGeneralInteractionStructure.Interaction = field(
        metadata={
            "name": "Interaction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    delivery: CapabilityGeneralInteractionStructure.Delivery = field(
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
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
    visit_numberis_order: None | bool = field(
        default=None,
        metadata={
            "name": "VisitNumberisOrder",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass(kw_only=True)
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

    @dataclass(kw_only=True)
    class Delivery:
        direct_delivery: bool = field(
            metadata={
                "name": "DirectDelivery",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            }
        )
        fetched_delivery: bool = field(
            metadata={
                "name": "FetchedDelivery",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            }
        )
