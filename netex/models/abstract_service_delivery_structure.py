from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

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


@dataclass(kw_only=True)
class AbstractServiceDeliveryStructure(ResponseStructure):
    choice: Sequence[
        MessageQualifierStructure
        | ParticipantRefStructure
        | SubscriptionFilterRefStructure
        | SubscriptionQualifierStructure
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RequestMessageRef",
                    "type": MessageQualifierStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "SubscriberRef",
                    "type": ParticipantRefStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "SubscriptionFilterRef",
                    "type": SubscriptionFilterRefStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "SubscriptionRef",
                    "type": SubscriptionQualifierStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
            "max_occurs": 3,
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
    valid_until: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "ValidUntil",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    shortest_possible_cycle: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "ShortestPossibleCycle",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    default_language: None | str = field(
        default=None,
        metadata={
            "name": "DefaultLanguage",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
