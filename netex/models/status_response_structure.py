from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime, XmlDuration

from .message_qualifier_structure import MessageQualifierStructure
from .participant_ref_structure import ParticipantRefStructure
from .response_structure import ResponseStructure
from .service_delivery_error_condition_structure import (
    ServiceDeliveryErrorConditionStructure,
)
from .status import Status
from .subscription_filter_ref_structure import SubscriptionFilterRefStructure
from .subscription_qualifier_structure import SubscriptionQualifierStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class StatusResponseStructure(ResponseStructure):
    request_message_ref: MessageQualifierStructure | None = field(
        default=None,
        metadata={
            "name": "RequestMessageRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscriber_ref: ParticipantRefStructure | None = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_filter_ref: SubscriptionFilterRefStructure | None = field(
        default=None,
        metadata={
            "name": "SubscriptionFilterRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_ref: SubscriptionQualifierStructure | None = field(
        default=None,
        metadata={
            "name": "SubscriptionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    status: Status | None = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    error_condition: ServiceDeliveryErrorConditionStructure | None = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    valid_until: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "ValidUntil",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    shortest_possible_cycle: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "ShortestPossibleCycle",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
