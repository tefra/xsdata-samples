from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.vms_message import VmsMessage

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsMessageIndexVmsMessage:
    class Meta:
        name = "_VmsMessageIndexVmsMessage"

    vms_message: Optional[VmsMessage] = field(
        default=None,
        metadata={
            "name": "vmsMessage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    message_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "messageIndex",
            "type": "Attribute",
            "required": True,
        },
    )
