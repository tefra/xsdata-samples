from __future__ import annotations

from dataclasses import dataclass, field

from .positive_integer import PositiveInteger
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class InitialSdDelayConfig:
    """
    This element is used to configure the offer behavior of the server and
    the find behavior on the client.

    :ivar initial_delay_max_value: @RESTRICT_TO_STANDARD:CP! Max Value
        in seconds to delay randomly the first offer (if aggregated by
        SdServerConfig) or the transmission of a find message (if
        aggregated by SdClientConfig). @END_RESTRICT_TO_STANDARD!
        @RESTRICT_TO_STANDARD:AP! Max Value in seconds to delay randomly
        the first offer (if aggregated in role initialOfferBehavior by
        SomeipSdServerServiceInstanceConfig) or the transmission of a
        find message (if aggregated in role initialFindBehavior by
        SomeipSdClientServiceInstanceConfig). @END_RESTRICT_TO_STANDARD!
    :ivar initial_delay_min_value: @RESTRICT_TO_STANDARD:CP! Min Value
        in seconds to delay randomly the first offer  or the
        transmission of a find message (if aggregated by
        SdClientConfig). @END_RESTRICT_TO_STANDARD!
        @RESTRICT_TO_STANDARD:AP! Min Value in seconds to delay randomly
        the first offer (if aggregated in role initialOfferBehavior by
        SomeipSdServerServiceInstanceConfig) or the transmission of a
        find message  (if aggregated in role initialFindBehavior by
        SomeipSdClientServiceInstanceConfig). @END_RESTRICT_TO_STANDARD!
    :ivar initial_repetitions_base_delay: @RESTRICT_TO_STANDARD:CP! The
        base delay for offer repetitions (if aggregated by
        SdServerConfig) or find repetitions (if aggregated by
        SdClientConfig). Successive find messages have an exponential
        back off delay. @END_RESTRICT_TO_STANDARD!
        @RESTRICT_TO_STANDARD:AP! The base delay for offer repetitions
        (if aggregated in role initialOfferBehavior by
        SomeipSdServerServiceInstanceConfig) or find repetitions (if
        aggregated in role initialFindBehavior by
        SomeipSdClientServiceInstanceConfig). Successive find messages
        have an exponential back off delay. @END_RESTRICT_TO_STANDARD!
    :ivar initial_repetitions_max: @RESTRICT_TO_STANDARD:CP! Describes
        the maximum amount of offer repetitions (if aggregated by
        SdServerConfig) or the maximum amount of find repetitions (if
        aggregated by SdClientConfig). @END_RESTRICT_TO_STANDARD!
        @RESTRICT_TO_STANDARD:AP! Describes the maximum amount of offer
        repetitions  (if aggregated in role initialOfferBehavior by
        SomeipSdServerServiceInstanceConfig) or the maximum amount of
        find repetitions (if aggregated in role initialFindBehavior by
        SomeipSdClientServiceInstanceConfig). @END_RESTRICT_TO_STANDARD!
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
        name = "INITIAL-SD-DELAY-CONFIG"

    initial_delay_max_value: TimeValue | None = field(
        default=None,
        metadata={
            "name": "INITIAL-DELAY-MAX-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    initial_delay_min_value: TimeValue | None = field(
        default=None,
        metadata={
            "name": "INITIAL-DELAY-MIN-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    initial_repetitions_base_delay: TimeValue | None = field(
        default=None,
        metadata={
            "name": "INITIAL-REPETITIONS-BASE-DELAY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    initial_repetitions_max: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "INITIAL-REPETITIONS-MAX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
