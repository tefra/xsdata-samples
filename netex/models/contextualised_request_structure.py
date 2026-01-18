from dataclasses import dataclass, field
from typing import Optional

from .message_qualifier_structure import MessageQualifierStructure
from .participant_ref_structure import ParticipantRefStructure
from .request_timestamp import RequestTimestamp
from .requestor_ref import RequestorRef
from .service_request_context_structure import ServiceRequestContextStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ContextualisedRequestStructure:
    service_request_context: ServiceRequestContextStructure | None = field(
        default=None,
        metadata={
            "name": "ServiceRequestContext",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_timestamp: RequestTimestamp | None = field(
        default=None,
        metadata={
            "name": "RequestTimestamp",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    account_id: str | None = field(
        default=None,
        metadata={
            "name": "AccountId",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    account_key: str | None = field(
        default=None,
        metadata={
            "name": "AccountKey",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
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
    delegator_address: str | None = field(
        default=None,
        metadata={
            "name": "DelegatorAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_ref: ParticipantRefStructure | None = field(
        default=None,
        metadata={
            "name": "DelegatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
