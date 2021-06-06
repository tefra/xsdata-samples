from dataclasses import dataclass, field
from typing import Optional
from .boolean import Boolean
from .diagnostic_event_window_time_enum import DiagnosticEventWindowTimeEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiagnosticEventWindow:
    """
    This represents the ability to define the characteristics of the applicable
    event window.

    :ivar event_window_time: This attribute clarifies the validity of
        the eventWindow
    :ivar storage_state_evaluation: If this attribute is set to TRUE the
        StorageStateBit will be evaluated if this EventWindowTime is
        requested.
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
        name = "DIAGNOSTIC-EVENT-WINDOW"

    event_window_time: Optional[DiagnosticEventWindowTimeEnum] = field(
        default=None,
        metadata={
            "name": "EVENT-WINDOW-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    storage_state_evaluation: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "STORAGE-STATE-EVALUATION",
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
