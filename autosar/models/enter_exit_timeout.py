from __future__ import annotations

from dataclasses import dataclass, field

from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EnterExitTimeout:
    """
    This meta-class represents the ability to specify a pair of timeouts,
    one for entering, and one for exiting.

    :ivar enter_timeout_value: This attribute represents the value of
        the enter timeout in seconds.
    :ivar exit_timeout_value: This attribute represents the value of the
        exit timeout in seconds.
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
        name = "ENTER-EXIT-TIMEOUT"

    enter_timeout_value: TimeValue | None = field(
        default=None,
        metadata={
            "name": "ENTER-TIMEOUT-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    exit_timeout_value: TimeValue | None = field(
        default=None,
        metadata={
            "name": "EXIT-TIMEOUT-VALUE",
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
