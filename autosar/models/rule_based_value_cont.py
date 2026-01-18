from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .ref import Ref
from .rule_based_value_specification import RuleBasedValueSpecification
from .unit_subtypes_enum import UnitSubtypesEnum
from .value_list import ValueList

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RuleBasedValueCont:
    """
    This represents the values of a compound primitive (CURVE, MAP, CUBOID,
    CUBE_4, CUBE_5, VAL_BLK) or an array.

    :ivar unit_ref: This represents the physical unit of the provided
        values.
    :ivar sw_arraysize: This attribute defines the size of each
        dimension for compound primitives CURVE, MAP, CUBOID, CUBE_4,
        CUBE_5, COM_AXIS, RES_AXIS, VAL_BLK. For each dimension one
        value has to be defined, e.g. one in case of COM_AXIS and two or
        more in case of MAP.
    :ivar rule_based_values: This represents the rule based value
        specification for the array or compound primitive (CURVE, MAP,
        CUBOID, CUBE_4, CUBE_5, VAL_BLK).
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
        name = "RULE-BASED-VALUE-CONT"

    unit_ref: RuleBasedValueCont.UnitRef | None = field(
        default=None,
        metadata={
            "name": "UNIT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_arraysize: ValueList | None = field(
        default=None,
        metadata={
            "name": "SW-ARRAYSIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rule_based_values: RuleBasedValueSpecification | None = field(
        default=None,
        metadata={
            "name": "RULE-BASED-VALUES",
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

    @dataclass
    class UnitRef(Ref):
        dest: UnitSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
