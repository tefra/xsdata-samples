from dataclasses import dataclass, field
from typing import Optional

from .numerical_value import NumericalValue
from .single_language_unit_names import SingleLanguageUnitNames

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PrmCharNumericalContents:
    """
    This metaclass represents the fact that it is a numerical parameter.

    :ivar abs: This represnts the absolute value of the parameter.
    :ivar tol: This represnts the tolerance of the parameter in the same
        units as the paramter: E.g. Tmperature= 50 +- 0.5 grad.
    :ivar min: This represnts the minimum value of the parameter.
    :ivar typ: This represnts the typical value of the parameter.
    :ivar max: This represnts the maximum value of the parameter.
    :ivar prm_unit: This is the measurement unit. Note that due to the
        fact that Prm is also available outside of MSRSW / AUTOSAR, this
        is not a formal reference  to a unit.
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
        name = "PRM-CHAR-NUMERICAL-CONTENTS"

    abs: NumericalValue | None = field(
        default=None,
        metadata={
            "name": "ABS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tol: NumericalValue | None = field(
        default=None,
        metadata={
            "name": "TOL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
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
    prm_unit: SingleLanguageUnitNames | None = field(
        default=None,
        metadata={
            "name": "PRM-UNIT",
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
