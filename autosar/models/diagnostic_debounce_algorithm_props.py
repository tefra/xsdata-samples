from __future__ import annotations

from dataclasses import dataclass, field

from .boolean import Boolean
from .diag_event_debounce_counter_based import DiagEventDebounceCounterBased
from .diag_event_debounce_monitor_internal import (
    DiagEventDebounceMonitorInternal,
)
from .diag_event_debounce_time_based import DiagEventDebounceTimeBased
from .diagnostic_debounce_behavior_enum_value_variation_point import (
    DiagnosticDebounceBehaviorEnumValueVariationPoint,
)
from .identifier import Identifier
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiagnosticDebounceAlgorithmProps:
    """
    Defines properties for the debounce algorithm class.

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar debounce_algorithm: This represents the actual debounce
        algorithm.
    :ivar debounce_behavior: This attribute defines how the event
        debounce algorithm will behave, if a related enable condition is
        not fulfilled or ControlDTCSetting of the related event is
        disabled.
    :ivar debounce_counter_storage: Switch to store the debounce counter
        value non-volatile or not. true: debounce counter value shall be
        stored non-volatile false: debounce counter value is volatile
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
        name = "DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS"

    short_name: Identifier | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: (
        DiagnosticDebounceAlgorithmProps.ShortNameFragments | None
    ) = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    debounce_algorithm: (
        DiagnosticDebounceAlgorithmProps.DebounceAlgorithm | None
    ) = field(
        default=None,
        metadata={
            "name": "DEBOUNCE-ALGORITHM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    debounce_behavior: (
        DiagnosticDebounceBehaviorEnumValueVariationPoint | None
    ) = field(
        default=None,
        metadata={
            "name": "DEBOUNCE-BEHAVIOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    debounce_counter_storage: Boolean | None = field(
        default=None,
        metadata={
            "name": "DEBOUNCE-COUNTER-STORAGE",
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

    @dataclass
    class ShortNameFragments:
        short_name_fragment: list[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class DebounceAlgorithm:
        diag_event_debounce_counter_based: (
            DiagEventDebounceCounterBased | None
        ) = field(
            default=None,
            metadata={
                "name": "DIAG-EVENT-DEBOUNCE-COUNTER-BASED",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diag_event_debounce_monitor_internal: (
            DiagEventDebounceMonitorInternal | None
        ) = field(
            default=None,
            metadata={
                "name": "DIAG-EVENT-DEBOUNCE-MONITOR-INTERNAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diag_event_debounce_time_based: DiagEventDebounceTimeBased | None = (
            field(
                default=None,
                metadata={
                    "name": "DIAG-EVENT-DEBOUNCE-TIME-BASED",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
