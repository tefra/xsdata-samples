from dataclasses import dataclass, field
from typing import List
from .response_endpoint_structure import ResponseEndpointStructure
from .termination_response_status_structure import (
    TerminationResponseStatusStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TerminateSubscriptionResponseStructure(ResponseEndpointStructure):
    termination_response_status: List[
        TerminationResponseStatusStructure
    ] = field(
        default_factory=list,
        metadata={
            "name": "TerminationResponseStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
