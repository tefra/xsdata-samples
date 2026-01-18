from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDateTime, XmlDuration

from .error_description_structure import ErrorDescriptionStructure
from .extensions_1 import Extensions1
from .other_error import OtherError
from .producer_request_endpoint_structure import (
    ProducerRequestEndpointStructure,
)
from .service_not_available_error import ServiceNotAvailableError
from .status import Status

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class HeartbeatNotificationStructure(ProducerRequestEndpointStructure):
    status: Status | None = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    data_ready: bool | None = field(
        default=None,
        metadata={
            "name": "DataReady",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    error_condition: HeartbeatNotificationStructure.ErrorCondition | None = field(
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
    service_started_time: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "ServiceStartedTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Extensions1 | None = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class ErrorCondition:
        service_not_available_error_or_other_error: ServiceNotAvailableError | OtherError | None = field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "ServiceNotAvailableError",
                        "type": ServiceNotAvailableError,
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
