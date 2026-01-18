from __future__ import annotations

from dataclasses import dataclass, field

from .consumer_request_endpoint_structure import (
    ConsumerRequestEndpointStructure,
)
from .message_ref_structure import MessageRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DataSupplyRequestStructure(ConsumerRequestEndpointStructure):
    notification_ref: None | MessageRefStructure = field(
        default=None,
        metadata={
            "name": "NotificationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    all_data: None | bool = field(
        default=None,
        metadata={
            "name": "AllData",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
