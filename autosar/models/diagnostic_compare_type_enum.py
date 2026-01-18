from __future__ import annotations

from dataclasses import dataclass, field

from .diagnostic_compare_type_enum_simple import (
    DiagnosticCompareTypeEnumSimple,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class DiagnosticCompareTypeEnum:
    """
    Enumeration for the type of a comparison of values usually expressed by
    the following operators: ==, !=, &lt;, &lt;=, &gt;, &gt;=.

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
        name = "DIAGNOSTIC-COMPARE-TYPE-ENUM"

    value: DiagnosticCompareTypeEnumSimple = field(
        metadata={
            "required": True,
        }
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
