from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.initial_sd_delay_config import InitialSdDelayConfig
from autosar.models.positive_integer import PositiveInteger
from autosar.models.request_response_delay import RequestResponseDelay
from autosar.models.tag_with_optional_value import TagWithOptionalValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SdClientConfig:
    """
    Client configuration for Service-Discovery.

    :ivar capability_records: A sequence of records to store arbitrary
        name/value pairs conveying additional information about the
        named service. Capability records shall only be existing if the
        respective SdClientConfig is composed by a
        ConsumedServiceInstance (see constr_3260).
    :ivar client_service_major_version: Major version number of the
        Service.
    :ivar client_service_minor_version: Minor version number of the
        Service.
    :ivar initial_find_behavior: Controls initial find behavior of
        clients.
    :ivar request_response_delay: Maximum/Minimum allowable response
        delay to entries received by multicast in seconds.
    :ivar ttl: TTL for Request and Subscribe messages.
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    """
    class Meta:
        name = "SD-CLIENT-CONFIG"

    capability_records: Optional["SdClientConfig.CapabilityRecords"] = field(
        default=None,
        metadata={
            "name": "CAPABILITY-RECORDS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    client_service_major_version: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "CLIENT-SERVICE-MAJOR-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    client_service_minor_version: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "CLIENT-SERVICE-MINOR-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    initial_find_behavior: Optional[InitialSdDelayConfig] = field(
        default=None,
        metadata={
            "name": "INITIAL-FIND-BEHAVIOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    request_response_delay: Optional[RequestResponseDelay] = field(
        default=None,
        metadata={
            "name": "REQUEST-RESPONSE-DELAY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    ttl: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "TTL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )

    @dataclass
    class CapabilityRecords:
        tag_with_optional_value: List[TagWithOptionalValue] = field(
            default_factory=list,
            metadata={
                "name": "TAG-WITH-OPTIONAL-VALUE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
