from __future__ import annotations

from dataclasses import dataclass, field

from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class DiagnosticParameterSupportInfo:
    """
    This represents a way to define which bit of the supportInfo is
    representing this part of the PID.

    :ivar support_info_bit: defines the bit in the SupportInfo byte,
        which represents the PID DataElement pidSize / position / size.
        Unit: byte.
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
        name = "DIAGNOSTIC-PARAMETER-SUPPORT-INFO"

    support_info_bit: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "SUPPORT-INFO-BIT",
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
