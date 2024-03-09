from dataclasses import dataclass, field
from typing import Optional

from .boolean import Boolean
from .limit_value import LimitValue
from .positive_integer import PositiveInteger
from .primitive_attribute_tailoring_subtypes_enum import (
    PrimitiveAttributeTailoringSubtypesEnum,
)
from .ref import Ref
from .regular_expression import RegularExpression

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PrimitiveAttributeCondition:
    """
    The PrimitiveAttributeCondition evaluates to true, if the referenced primitive
    attribute is accepted by all rules of this condition.

    :ivar lower_multiplicity: Specifies the minimal number of times an
        object shall occur. If this primitive attribute is not set, then
        the object is optional.
    :ivar upper_multiplicity: Specifies the maximum number of times an
        object may occur.  If this primitive attribute is not set, then
        there is no limit with respect to the maximum occurrence.
    :ivar upper_multiplicity_infinite: This explicitly specifies, that
        the upper multiplicity is NOT restricted. Note: The use of
        'upperMultiplicityInfinite' and 'upperMultiplicity' is mutual
        exclusive.
    :ivar max: Specifies the upper bounds for numeric values.
    :ivar max_length: Specifies the maximum number of characters of
        textual values.
    :ivar min: Specifies the lower bounds for numeric values.
    :ivar min_length: Specifies the minimal number of characters of
        textual values.
    :ivar pattern: Defines the exact sequence of characters that are
        acceptable.
    :ivar attribute_ref: The primitive attribute that has to be accepted
        by the restrictions of this PrimitiveAttributeCondition
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
        name = "PRIMITIVE-ATTRIBUTE-CONDITION"

    lower_multiplicity: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "LOWER-MULTIPLICITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    upper_multiplicity: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "UPPER-MULTIPLICITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    upper_multiplicity_infinite: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "UPPER-MULTIPLICITY-INFINITE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max: Optional[LimitValue] = field(
        default=None,
        metadata={
            "name": "MAX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_length: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MAX-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    min: Optional[LimitValue] = field(
        default=None,
        metadata={
            "name": "MIN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    min_length: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MIN-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pattern: Optional[RegularExpression] = field(
        default=None,
        metadata={
            "name": "PATTERN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    attribute_ref: Optional["PrimitiveAttributeCondition.AttributeRef"] = (
        field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
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

    @dataclass
    class AttributeRef(Ref):
        dest: Optional[PrimitiveAttributeTailoringSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
