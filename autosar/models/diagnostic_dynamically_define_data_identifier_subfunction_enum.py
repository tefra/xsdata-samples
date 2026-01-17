from dataclasses import dataclass, field
from typing import Optional

from .diagnostic_dynamically_define_data_identifier_subfunction_enum_simple import (
    DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnumSimple,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum:
    """
    This meta-class contains a list of possible subfunctions for the UDS
    service 0x2C.

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
        name = "DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER-SUBFUNCTION-ENUM"

    value: Optional[
        DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnumSimple
    ] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
