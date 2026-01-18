from __future__ import annotations

from dataclasses import dataclass, field

from .interval_type_enum_simple import IntervalTypeEnumSimple

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class LimitValue:
    """
    This class represents the ability to express a numerical limit.

    Note that this is in fact a NumericalVariationPoint but has the
    additional attribute intervalType.

    :ivar value:
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
    :ivar interval_type: This specifies the type of the interval. If the
        attribute is missing the interval shall be considered as
        "CLOSED".
    """

    class Meta:
        name = "LIMIT-VALUE"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"(0[xX][0-9a-fA-F]+)|(0[0-7]+)|(0[bB][0-1]+)|(([+\-]?[1-9][0-9]+(\.[0-9]+)?|[+\-]?[0-9](\.[0-9]+)?)([eE]([+\-]?)[0-9]+)?)|\.0|INF|-INF|NaN",
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
    interval_type: None | IntervalTypeEnumSimple = field(
        default=None,
        metadata={
            "name": "INTERVAL-TYPE",
            "type": "Attribute",
        },
    )
