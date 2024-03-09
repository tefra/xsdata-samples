from dataclasses import dataclass, field
from typing import Optional

from .aggregation_tailoring_subtypes_enum import (
    AggregationTailoringSubtypesEnum,
)
from .boolean import Boolean
from .positive_integer import PositiveInteger
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class AggregationCondition:
    """
    The AggregationCondition evaluates to true, if the referenced aggregation is
    accepted by all rules of this condition.

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
    :ivar aggregation_ref: The aggregation that has to be accepted by
        the restrictions of this AggregationCondition
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
        name = "AGGREGATION-CONDITION"

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
    aggregation_ref: Optional["AggregationCondition.AggregationRef"] = field(
        default=None,
        metadata={
            "name": "AGGREGATION-REF",
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

    @dataclass
    class AggregationRef(Ref):
        dest: Optional[AggregationTailoringSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
