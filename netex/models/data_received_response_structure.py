from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Union

from .consumer_response_endpoint_structure import (
    ConsumerResponseEndpointStructure,
)
from .error_description_structure import ErrorDescriptionStructure
from .other_error import OtherError
from .status import Status
from .unknown_subscription_error import UnknownSubscriptionError

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DataReceivedResponseStructure(ConsumerResponseEndpointStructure):
    status: Status | None = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    error_condition: DataReceivedResponseStructure.ErrorCondition | None = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class ErrorCondition:
        unknown_subscription_error_or_other_error: UnknownSubscriptionError | OtherError | None = field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
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
        description: ErrorDescriptionStructure | None = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
