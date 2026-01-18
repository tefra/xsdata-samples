from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .response_endpoint_structure import ResponseEndpointStructure
from .termination_response_status_structure import (
    TerminationResponseStatusStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TerminateSubscriptionResponseStructure(ResponseEndpointStructure):
    termination_response_status: Iterable[
        TerminationResponseStatusStructure
    ] = field(
        default_factory=list,
        metadata={
            "name": "TerminationResponseStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
