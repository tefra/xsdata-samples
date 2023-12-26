from dataclasses import dataclass, field
from typing import Optional
from .annotation import VariationPoint
from .numerical_value_variation_point import NumericalValueVariationPoint
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class NumericalOrText:
    """This meta-class represents the ability to yield either a numerical or a
    string.

    A typical use case is that two or more instances of this meta-class
    are aggregated with a VariationPoint where some instances yield
    strings while other instances yield numerical depending on the
    resolution of the binding expression.

    :ivar vf: This attribute represents the ability to provide a
        numerical value. The latest binding time of the VariationPoint
        shall be preCompileTime.
    :ivar vt: This attribute represents the ability to provide a textual
        value.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "NUMERICAL-OR-TEXT"

    vf: Optional[NumericalValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "VF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    vt: Optional[String] = field(
        default=None,
        metadata={
            "name": "VT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
