from __future__ import annotations

from dataclasses import dataclass, field

from .numerical_value_variation_point import NumericalValueVariationPoint

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TextTableValuePair:
    """
    Defines a pair of text values which are translated into each other.

    :ivar first_value: Value of first DataPrototype provided similar to
        a numerical ValueSpecification which is intended to be assigned
        to a Primitive data element. Note that the numerical value is a
        variant, it can be computed by a formula.
    :ivar second_value: Value of second DataPrototype provided similar
        to a numerical  ValueSpecification which is intended to be
        assigned to a Primitive data element. Note that the numerical
        value is a variant, it can be computed by a formula.
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
        name = "TEXT-TABLE-VALUE-PAIR"

    first_value: None | NumericalValueVariationPoint = field(
        default=None,
        metadata={
            "name": "FIRST-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    second_value: None | NumericalValueVariationPoint = field(
        default=None,
        metadata={
            "name": "SECOND-VALUE",
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
