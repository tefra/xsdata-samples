from __future__ import annotations

from dataclasses import dataclass, field

from .capability_not_supported_error import CapabilityNotSupportedError
from .error_description_structure import ErrorDescriptionStructure
from .message_qualifier_structure import MessageQualifierStructure
from .other_error import OtherError
from .participant_ref_structure import ParticipantRefStructure
from .response_timestamp import ResponseTimestamp
from .status import Status
from .subscription_filter_ref_structure import SubscriptionFilterRefStructure
from .subscription_qualifier_structure import SubscriptionQualifierStructure
from .unknown_subscriber_error import UnknownSubscriberError
from .unknown_subscription_error import UnknownSubscriptionError

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TerminationResponseStatusStructure:
    response_timestamp: None | ResponseTimestamp = field(
        default=None,
        metadata={
            "name": "ResponseTimestamp",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_message_ref: None | MessageQualifierStructure = field(
        default=None,
        metadata={
            "name": "RequestMessageRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscriber_ref: None | ParticipantRefStructure = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_filter_ref: None | SubscriptionFilterRefStructure = field(
        default=None,
        metadata={
            "name": "SubscriptionFilterRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_ref: None | SubscriptionQualifierStructure = field(
        default=None,
        metadata={
            "name": "SubscriptionRef",
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
            "required": True,
        },
    )
    error_condition: (
        None | TerminationResponseStatusStructure.ErrorCondition
    ) = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class ErrorCondition:
        choice: (
            None
            | CapabilityNotSupportedError
            | UnknownSubscriberError
            | UnknownSubscriptionError
            | OtherError
        ) = field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "CapabilityNotSupportedError",
                        "type": CapabilityNotSupportedError,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "UnknownSubscriberError",
                        "type": UnknownSubscriberError,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "UnknownSubscriptionError",
                        "type": UnknownSubscriptionError,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "OtherError",
                        "type": OtherError,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                ),
            },
        )
        description: None | ErrorDescriptionStructure = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
