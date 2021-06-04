from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CapabilityGeneralInteractionStructure:
    interaction: Optional["CapabilityGeneralInteractionStructure.Interaction"] = field(
        default=None,
        metadata={
            "name": "Interaction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    delivery: Optional["CapabilityGeneralInteractionStructure.Delivery"] = field(
        default=None,
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
        }
    )
    multiple_subscriber_filter: bool = field(
        default=False,
        metadata={
            "name": "MultipleSubscriberFilter",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    has_confirm_delivery: bool = field(
        default=False,
        metadata={
            "name": "HasConfirmDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    has_heartbeat: bool = field(
        default=False,
        metadata={
            "name": "HasHeartbeat",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    visit_numberis_order: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VisitNumberisOrder",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )

    @dataclass
    class Interaction:
        request_response: bool = field(
            default=True,
            metadata={
                "name": "RequestResponse",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            }
        )
        publish_subscribe: bool = field(
            default=True,
            metadata={
                "name": "PublishSubscribe",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            }
        )

    @dataclass
    class Delivery:
        direct_delivery: Optional[bool] = field(
            default=None,
            metadata={
                "name": "DirectDelivery",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            }
        )
        fetched_delivery: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FetchedDelivery",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            }
        )
