from dataclasses import dataclass, field
from typing import Optional

from .message_ref_structure import MessageRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DataSupplyRequestBodyStructure:
    notification_ref: Optional[MessageRefStructure] = field(
        default=None,
        metadata={
            "name": "NotificationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    all_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllData",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
