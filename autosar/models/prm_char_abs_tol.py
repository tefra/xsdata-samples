from dataclasses import dataclass, field
from typing import Optional
from autosar.models.numerical_value import NumericalValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PrmCharAbsTol:
    """
    The parameter is specified as ablolute value with a tolerance.

    :ivar abs: This represnts the absolute value of the parameter.
    :ivar tol: This represnts the tolerance of the parameter in the same
        units as the paramter: E.g. Tmperature= 50 +- 0.5 grad.
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
        name = "PRM-CHAR-ABS-TOL"

    abs: Optional[NumericalValue] = field(
        default=None,
        metadata={
            "name": "ABS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tol: Optional[NumericalValue] = field(
        default=None,
        metadata={
            "name": "TOL",
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
