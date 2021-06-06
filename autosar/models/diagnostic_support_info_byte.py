from dataclasses import dataclass, field
from typing import Optional
from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiagnosticSupportInfoByte:
    """
    This meta-class defines the support information (typically byte A) to
    declare the usability of the DataElements within the so-called packeted
    PIDs (e.g. PID$68).

    :ivar position: This represents the position of the supportInfo in
        the PID. Unit: byte.
    :ivar size: This represents the size of the supportInfo within the
        PID. Unit: byte.
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
        name = "DIAGNOSTIC-SUPPORT-INFO-BYTE"

    position: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "POSITION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    size: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "SIZE",
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
