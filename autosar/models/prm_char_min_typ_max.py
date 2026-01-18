from dataclasses import dataclass, field
from typing import Optional

from .numerical_value import NumericalValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PrmCharMinTypMax:
    """
    This metaclass represents the characteristics of a parameter as
    minimal, typical maximum value.

    :ivar min: This represnts the minimum value of the parameter.
    :ivar typ: This represnts the typical value of the parameter.
    :ivar max: This represnts the maximum value of the parameter.
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
        name = "PRM-CHAR-MIN-TYP-MAX"

    min: NumericalValue | None = field(
        default=None,
        metadata={
            "name": "MIN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    typ: NumericalValue | None = field(
        default=None,
        metadata={
            "name": "TYP",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max: NumericalValue | None = field(
        default=None,
        metadata={
            "name": "MAX",
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
