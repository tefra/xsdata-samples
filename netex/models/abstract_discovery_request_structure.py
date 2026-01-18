from __future__ import annotations

from dataclasses import dataclass, field

from .authenticated_request_structure import AuthenticatedRequestStructure
from .message_qualifier_structure import MessageQualifierStructure
from .requestor_ref import RequestorRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractDiscoveryRequestStructure(AuthenticatedRequestStructure):
    address: None | str = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    requestor_ref: RequestorRef = field(
        metadata={
            "name": "RequestorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    message_identifier: None | MessageQualifierStructure = field(
        default=None,
        metadata={
            "name": "MessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
