from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from .extensions_1 import Extensions1
from .other_error import OtherError
from .producer_request_endpoint_structure import ProducerRequestEndpointStructure
from .service_not_available_error import ServiceNotAvailableError

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class HeartbeatNotificationStructure(ProducerRequestEndpointStructure):
    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    data_ready: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DataReady",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    error_condition: Optional["HeartbeatNotificationStructure.ErrorCondition"] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    valid_until: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ValidUntil",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    shortest_possible_cycle: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ShortestPossibleCycle",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    service_started_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ServiceStartedTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )

    @dataclass
    class ErrorCondition:
        service_not_available_error: Optional[ServiceNotAvailableError] = field(
            default=None,
            metadata={
                "name": "ServiceNotAvailableError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            }
        )
        other_error: Optional[OtherError] = field(
            default=None,
            metadata={
                "name": "OtherError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
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