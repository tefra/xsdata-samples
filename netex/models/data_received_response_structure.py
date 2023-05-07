from dataclasses import dataclass, field
from typing import Optional
from .consumer_response_endpoint_structure import ConsumerResponseEndpointStructure
from .other_error import OtherError
from .unknown_subscription_error import UnknownSubscriptionError

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DataReceivedResponseStructure(ConsumerResponseEndpointStructure):
    status: bool = field(
        default=True,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    error_condition: Optional["DataReceivedResponseStructure.ErrorCondition"] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )

    @dataclass
    class ErrorCondition:
        unknown_subscription_error_or_other_error: Optional[object] = field(
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
            }
        )
        description: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            }
        )
