from dataclasses import dataclass, field
from typing import Optional
from autosar.models.numerical_value import NumericalValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CompuConstNumericContent:
    """This meta-class represents the fact that the constant value of the
    computation method is a numerical value.

    It is separated from CompuConstFormulaContent to support
    compatibility with ASAM HDO.

    :ivar v: This represents the numerical value.
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
        name = "COMPU-CONST-NUMERIC-CONTENT"

    v: Optional[NumericalValue] = field(
        default=None,
        metadata={
            "name": "V",
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
