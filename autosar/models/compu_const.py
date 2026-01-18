from __future__ import annotations

from dataclasses import dataclass, field

from .numerical_value import NumericalValue
from .numerical_value_variation_point import NumericalValueVariationPoint
from .verbatim_string import VerbatimString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CompuConst:
    """
    This meta-class represents the fact that the value of a computation
    method scale is constant.

    :ivar vf: Value calculated via a system constant. This element is
        included in every case where parameters should be generated from
        numerical values during compile time (not runtime!). Thus for
        example, the influence of the cylinder number on conversion
        formulae can be introduced in a repeatable manner.
    :ivar v: This represents the numerical value.
    :ivar vt: This represents a textual constant in the computation
        method.
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
        name = "COMPU-CONST"

    vf: None | NumericalValueVariationPoint = field(
        default=None,
        metadata={
            "name": "VF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    v: None | NumericalValue = field(
        default=None,
        metadata={
            "name": "V",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    vt: None | VerbatimString = field(
        default=None,
        metadata={
            "name": "VT",
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
