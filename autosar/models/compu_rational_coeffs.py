from dataclasses import dataclass, field
from typing import Optional

from .compu_nominator_denominator import CompuNominatorDenominator

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CompuRationalCoeffs:
    """
    This meta-class represents the ability to express a rational function
    by specifying the coefficients of nominator and denominator.

    :ivar compu_numerator: This is the numerator of the rational
        expression.
    :ivar compu_denominator: This is the denominator of the expression.
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
        name = "COMPU-RATIONAL-COEFFS"

    compu_numerator: CompuNominatorDenominator | None = field(
        default=None,
        metadata={
            "name": "COMPU-NUMERATOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    compu_denominator: CompuNominatorDenominator | None = field(
        default=None,
        metadata={
            "name": "COMPU-DENOMINATOR",
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
