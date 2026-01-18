from __future__ import annotations

from dataclasses import dataclass, field

from .initial_sd_delay_config import InitialSdDelayConfig
from .positive_integer import PositiveInteger
from .request_response_delay import RequestResponseDelay
from .tag_with_optional_value import TagWithOptionalValue
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SdServerConfig:
    """
    Server configuration for Service-Discovery.

    :ivar capability_records: A sequence of records to store arbitrary
        name/value pairs conveying additional information about the
        named service. Capability records shall only be existing if the
        respective SdServerConfig is composed by a
        ProvidedServiceInstance (see constr_3259).
    :ivar initial_offer_behavior: Controls offer behavior of the server.
    :ivar offer_cyclic_delay: Optional attribute to define cyclic
        offers. Cyclic offer is active, if the delay is set (in
        seconds).
    :ivar request_response_delay: Maximum/Minimum allowable response
        delay to entries received by multicast in seconds.
    :ivar server_service_major_version: Major version number of the
        Service.
    :ivar server_service_minor_version: Minor version number of the
        Service.
    :ivar ttl: Time to live. Shall be a positive value (sInt32).
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
        name = "SD-SERVER-CONFIG"

    capability_records: None | SdServerConfig.CapabilityRecords = field(
        default=None,
        metadata={
            "name": "CAPABILITY-RECORDS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    initial_offer_behavior: None | InitialSdDelayConfig = field(
        default=None,
        metadata={
            "name": "INITIAL-OFFER-BEHAVIOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    offer_cyclic_delay: None | TimeValue = field(
        default=None,
        metadata={
            "name": "OFFER-CYCLIC-DELAY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    request_response_delay: None | RequestResponseDelay = field(
        default=None,
        metadata={
            "name": "REQUEST-RESPONSE-DELAY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    server_service_major_version: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "SERVER-SERVICE-MAJOR-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    server_service_minor_version: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "SERVER-SERVICE-MINOR-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ttl: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "TTL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class CapabilityRecords:
        tag_with_optional_value: list[TagWithOptionalValue] = field(
            default_factory=list,
            metadata={
                "name": "TAG-WITH-OPTIONAL-VALUE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
