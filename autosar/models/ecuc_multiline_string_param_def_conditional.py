from dataclasses import dataclass, field
from typing import Optional

from .admin_data import VariationPoint
from .positive_integer import PositiveInteger
from .regular_expression import RegularExpression
from .verbatim_string import VerbatimString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EcucMultilineStringParamDefConditional:
    """
    This element was generated/modified due to an atpVariation stereotype.

    :ivar default_value: Default value of the string configuration
        parameter.
    :ivar max_length: Max length allowed for this string.
    :ivar min_length: Min length allowed for this string.
    :ivar regular_expression: This represents the regular expression
        which shall be used to validate the string parameter value.
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
        name = "ECUC-MULTILINE-STRING-PARAM-DEF-CONDITIONAL"

    default_value: VerbatimString | None = field(
        default=None,
        metadata={
            "name": "DEFAULT-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_length: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "MAX-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    min_length: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "MIN-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    regular_expression: RegularExpression | None = field(
        default=None,
        metadata={
            "name": "REGULAR-EXPRESSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: VariationPoint | None = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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
