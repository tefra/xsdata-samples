from dataclasses import dataclass, field
from typing import Optional

from .numerical_value_variation_point import NumericalValueVariationPoint

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CompuConstFormulaContent:
    """
    This meta-class represents the fact that the constant value of the
    computation method is represented by a variation point.

    This difference is due to compatibility with ASAM HDO.

    :ivar vf: Value calculated via a system constant. This element is
        included in every case where parameters should be generated from
        numerical values during compile time (not runtime!). Thus for
        example, the influence of the cylinder number on conversion
        formulae can be introduced in a repeatable manner.
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
        name = "COMPU-CONST-FORMULA-CONTENT"

    vf: NumericalValueVariationPoint | None = field(
        default=None,
        metadata={
            "name": "VF",
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
