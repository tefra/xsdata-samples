from dataclasses import dataclass, field
from typing import List
from .capabilities_request import CapabilitiesRequest
from .capabilities_response import CapabilitiesResponse
from .check_status_request import CheckStatusRequest
from .check_status_response import CheckStatusResponse
from .data_ready_acknowledgement import DataReadyAcknowledgement
from .data_ready_notification import DataReadyNotification
from .data_received_acknowledgement import DataReceivedAcknowledgement
from .data_supply_request import DataSupplyRequest
from .extensions_1 import Extensions1
from .heartbeat_notification import HeartbeatNotification
from .service_delivery import ServiceDelivery
from .service_request import ServiceRequest
from .subscription_request import SubscriptionRequest
from .subscription_response import SubscriptionResponse
from .terminate_subscription_request import TerminateSubscriptionRequest
from .terminate_subscription_response import TerminateSubscriptionResponse

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SiriSchema:
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceRequest",
                    "type": ServiceRequest,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "SubscriptionRequest",
                    "type": SubscriptionRequest,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "TerminateSubscriptionRequest",
                    "type": TerminateSubscriptionRequest,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "DataReadyNotification",
                    "type": DataReadyNotification,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "DataSupplyRequest",
                    "type": DataSupplyRequest,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "CheckStatusRequest",
                    "type": CheckStatusRequest,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "HeartbeatNotification",
                    "type": HeartbeatNotification,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "CapabilitiesRequest",
                    "type": CapabilitiesRequest,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "SubscriptionResponse",
                    "type": SubscriptionResponse,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "TerminateSubscriptionResponse",
                    "type": TerminateSubscriptionResponse,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "DataReadyAcknowledgement",
                    "type": DataReadyAcknowledgement,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ServiceDelivery",
                    "type": ServiceDelivery,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "DataReceivedAcknowledgement",
                    "type": DataReceivedAcknowledgement,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "CheckStatusResponse",
                    "type": CheckStatusResponse,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "CapabilitiesResponse",
                    "type": CapabilitiesResponse,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "Extensions",
                    "type": Extensions1,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
            "max_occurs": 8,
        }
    )
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        }
    )
