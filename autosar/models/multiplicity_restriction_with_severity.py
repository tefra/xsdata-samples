from __future__ import annotations

from dataclasses import dataclass, field

from .boolean import Boolean
from .positive_integer import PositiveInteger
from .severity_enum import SeverityEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class MultiplicityRestrictionWithSeverity:
    """
    Restriction that specifies the valid number of occurrences of an
    element in the current context.

    :ivar severity: Severity level that is reported in case the
        restriction is violated.
    :ivar lower_multiplicity: Specifies the minimal number of times an
        object shall occur. If this primitive attribute is not set, then
        the object is optional.
    :ivar upper_multiplicity: Specifies the maximum number of times an
        object may occur.  If this primitive attribute is not set, then
        there is no limit with respect to the maximum occurrence.
    :ivar upper_multiplicity_infinite: This explicitly specifies, that
        the upper multiplicity is NOT restricted. Note: The use of
        'upperMultiplicityInfinite' and 'upperMultiplicity' is mutual
        exclusive.
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
        name = "MULTIPLICITY-RESTRICTION-WITH-SEVERITY"

    severity: SeverityEnum | None = field(
        default=None,
        metadata={
            "name": "SEVERITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    lower_multiplicity: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "LOWER-MULTIPLICITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    upper_multiplicity: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "UPPER-MULTIPLICITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    upper_multiplicity_infinite: Boolean | None = field(
        default=None,
        metadata={
            "name": "UPPER-MULTIPLICITY-INFINITE",
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
