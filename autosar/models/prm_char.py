from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import DocumentationBlock
from .numerical_value import NumericalValue
from .single_language_unit_names import SingleLanguageUnitNames
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PrmChar:
    """
    This metaclass represents the ability to express the characteristics of
    one particular parameter.

    It can be exressed as numerical or as text parameter (provided as
    subclasses of PrmCharContents).

    :ivar cond: This represents the particular conditions under which
        the parameter characteristic is valid.
    :ivar abs: This represnts the absolute value of the parameter.
    :ivar tol: This represnts the tolerance of the parameter in the same
        units as the paramter: E.g. Tmperature= 50 +- 0.5 grad.
    :ivar min: This represnts the minimum value of the parameter.
    :ivar typ: This represnts the typical value of the parameter.
    :ivar max: This represnts the maximum value of the parameter.
    :ivar prm_unit: This is the measurement unit. Note that due to the
        fact that Prm is also available outside of MSRSW / AUTOSAR, this
        is not a formal reference  to a unit.
    :ivar text: This is the value of a textual parameter
    :ivar remark: This represents further remarks about the particular
        parameter characteristics.
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
        name = "PRM-CHAR"

    cond: None | DocumentationBlock = field(
        default=None,
        metadata={
            "name": "COND",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    abs: None | NumericalValue = field(
        default=None,
        metadata={
            "name": "ABS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tol: None | NumericalValue = field(
        default=None,
        metadata={
            "name": "TOL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    min: None | NumericalValue = field(
        default=None,
        metadata={
            "name": "MIN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    typ: None | NumericalValue = field(
        default=None,
        metadata={
            "name": "TYP",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max: None | NumericalValue = field(
        default=None,
        metadata={
            "name": "MAX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    prm_unit: None | SingleLanguageUnitNames = field(
        default=None,
        metadata={
            "name": "PRM-UNIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    text: None | String = field(
        default=None,
        metadata={
            "name": "TEXT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    remark: None | DocumentationBlock = field(
        default=None,
        metadata={
            "name": "REMARK",
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
