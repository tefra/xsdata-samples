from __future__ import annotations

from dataclasses import dataclass, field

from .compu_rational_coeffs import CompuRationalCoeffs

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CompuScaleRationalFormula:
    """
    This meta-class represents the fact that the computation in this scale
    is represented as rational term.

    :ivar compu_rational_coeffs: This specifies the coefficients of the
        rational formula.
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
        name = "COMPU-SCALE-RATIONAL-FORMULA"

    compu_rational_coeffs: None | CompuRationalCoeffs = field(
        default=None,
        metadata={
            "name": "COMPU-RATIONAL-COEFFS",
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
