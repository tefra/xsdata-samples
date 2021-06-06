from dataclasses import dataclass, field
from typing import List, Optional
from .numerical_value_variation_point import NumericalValueVariationPoint

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CompuNominatorDenominator:
    """
    This class represents the ability to express a polynomial either as
    Nominator or as Denominator.

    :ivar v: this is the list of polynomial factors. Note that the first
        vf represents the power=0.  The polynomial is v[0] * x^0 + v[1]
        * x^1 ...
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
        name = "COMPU-NOMINATOR-DENOMINATOR"

    v: List[NumericalValueVariationPoint] = field(
        default_factory=list,
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
