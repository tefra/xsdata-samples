from dataclasses import dataclass, field
from typing import Optional

from .limit_value import LimitValue
from .positive_integer import PositiveInteger
from .regular_expression import RegularExpression
from .severity_enum import SeverityEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ValueRestrictionWithSeverity:
    """
    Specifies valid values of primitive data types.

    A value is valid if all rules defined by this ValueRestriction evaluate
    to true.

    :ivar severity: Severity level that is reported in case the
        restriction is violated.
    :ivar max: Specifies the upper bounds for numeric values.
    :ivar max_length: Specifies the maximum number of characters of
        textual values.
    :ivar min: Specifies the lower bounds for numeric values.
    :ivar min_length: Specifies the minimal number of characters of
        textual values.
    :ivar pattern: Defines the exact sequence of characters that are
        acceptable.
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
        name = "VALUE-RESTRICTION-WITH-SEVERITY"

    severity: SeverityEnum | None = field(
        default=None,
        metadata={
            "name": "SEVERITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max: LimitValue | None = field(
        default=None,
        metadata={
            "name": "MAX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_length: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "MAX-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    min: LimitValue | None = field(
        default=None,
        metadata={
            "name": "MIN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    min_length: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "MIN-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pattern: RegularExpression | None = field(
        default=None,
        metadata={
            "name": "PATTERN",
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
