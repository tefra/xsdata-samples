from dataclasses import dataclass, field
from typing import Optional
from .response_structure import ResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ResponseEndpointStructure(ResponseStructure):
    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    responder_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResponderRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    request_message_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestMessageRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    delegator_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    delegator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
