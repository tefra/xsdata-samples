from __future__ import annotations

from dataclasses import dataclass, field

from .diagnostic_obd_support_enum_simple import DiagnosticObdSupportEnumSimple

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiagnosticObdSupportEnum:
    """
    This meta-class represents the ability to model the roles in which a
    participation in OBD is foreseen.

    At the moment, this applies exclusively to the Dem. However, future
    extension of the Dcm may require this setting as well.

    :ivar value:
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
        name = "DIAGNOSTIC-OBD-SUPPORT-ENUM"

    value: None | DiagnosticObdSupportEnumSimple = field(
        default=None,
        metadata={
            "required": True,
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
