from dataclasses import dataclass, field
from typing import Optional

from .authenticated_request_structure import AuthenticatedRequestStructure
from .message_qualifier_structure import MessageQualifierStructure
from .requestor_ref import RequestorRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractDiscoveryRequestStructure(AuthenticatedRequestStructure):
    address: str | None = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    requestor_ref: RequestorRef | None = field(
        default=None,
        metadata={
            "name": "RequestorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    message_identifier: MessageQualifierStructure | None = field(
        default=None,
        metadata={
            "name": "MessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
