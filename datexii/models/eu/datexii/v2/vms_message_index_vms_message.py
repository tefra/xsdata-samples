from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.vms_message import VmsMessage

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class VmsMessageIndexVmsMessage:
    class Meta:
        name = "_VmsMessageIndexVmsMessage"

    vms_message: VmsMessage = field(
        metadata={
            "name": "vmsMessage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    message_index: int = field(
        metadata={
            "name": "messageIndex",
            "type": "Attribute",
            "required": True,
        }
    )
