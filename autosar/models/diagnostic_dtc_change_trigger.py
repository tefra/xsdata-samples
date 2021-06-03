from dataclasses import dataclass, field
from typing import Optional
from autosar.models.diagnostic_initial_event_status_enum import DiagnosticInitialEventStatusEnum
from autosar.models.positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiagnosticDtcChangeTrigger:
    """
    This represents the ability to define a trigger that executes on the change
    of any DiagnosticTroubleCode.

    :ivar initial_event_status: This represents the initial status of
        the enclosing DiagnosticResponseOnEventTrigger.
    :ivar dtc_status_mask: This attribute represents the ability to
        define a status mask for the triggering of an ROE response on
        the change of a DTC.
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
        name = "DIAGNOSTIC-DTC-CHANGE-TRIGGER"

    initial_event_status: Optional[DiagnosticInitialEventStatusEnum] = field(
        default=None,
        metadata={
            "name": "INITIAL-EVENT-STATUS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    dtc_status_mask: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "DTC-STATUS-MASK",
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
