from dataclasses import dataclass, field
from typing import Optional

from .consumer_request_endpoint_structure import (
    ConsumerRequestEndpointStructure,
)
from .message_ref_structure import MessageRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DataSupplyRequestStructure(ConsumerRequestEndpointStructure):
    notification_ref: MessageRefStructure | None = field(
        default=None,
        metadata={
            "name": "NotificationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    all_data: bool | None = field(
        default=None,
        metadata={
            "name": "AllData",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
