from __future__ import annotations

from dataclasses import dataclass, field

from .message_qualifier_structure import MessageQualifierStructure
from .participant_ref_structure import ParticipantRefStructure
from .response_structure import ResponseStructure
from .service_delivery_error_condition_structure import (
    ServiceDeliveryErrorConditionStructure,
)
from .status import Status

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractServiceCapabilitiesResponseStructure(ResponseStructure):
    request_message_ref: None | MessageQualifierStructure = field(
        default=None,
        metadata={
            "name": "RequestMessageRef",
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
    status: None | Status = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    error_condition: None | ServiceDeliveryErrorConditionStructure = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
