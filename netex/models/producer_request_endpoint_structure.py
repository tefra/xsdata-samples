from __future__ import annotations

from dataclasses import dataclass, field

from .authenticated_request_structure import AuthenticatedRequestStructure
from .message_qualifier_structure import MessageQualifierStructure
from .participant_ref_structure import ParticipantRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ProducerRequestEndpointStructure(AuthenticatedRequestStructure):
    address: None | str = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    producer_ref: None | ParticipantRefStructure = field(
        default=None,
        metadata={
            "name": "ProducerRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    message_identifier: None | MessageQualifierStructure = field(
        default=None,
        metadata={
            "name": "MessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_address: None | str = field(
        default=None,
        metadata={
            "name": "DelegatorAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_ref: None | ParticipantRefStructure = field(
        default=None,
        metadata={
            "name": "DelegatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
