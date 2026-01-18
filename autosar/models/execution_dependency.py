from __future__ import annotations

from dataclasses import dataclass, field

from .mode_in_process_instance_ref import ModeInProcessInstanceRef

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ExecutionDependency:
    """
    This element defines a ProcessState in which a dependent process needs
    to be before the process that aggregates the ExecutionDependency
    element can be started.

    :ivar process_state_iref: This represent the applicable
        modeDeclaration that represents an ProcessState.
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
        name = "EXECUTION-DEPENDENCY"

    process_state_iref: ModeInProcessInstanceRef | None = field(
        default=None,
        metadata={
            "name": "PROCESS-STATE-IREF",
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
