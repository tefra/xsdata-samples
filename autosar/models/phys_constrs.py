from dataclasses import dataclass, field
from typing import List, Optional

from .limit import Limit
from .monotony_enum import MonotonyEnum
from .numerical_value import NumericalValue
from .ref import Ref
from .scale_constr import ScaleConstr
from .unit_subtypes_enum import UnitSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PhysConstrs:
    """This meta-class represents the ability to express physical constraints.

    Therefore it has (in opposite to InternalConstrs) a reference to a
    Unit.

    :ivar lower_limit: This specifies the lower limit of the constraint.
    :ivar upper_limit: This specifies the upper limit of the constraint.
    :ivar scale_constrs: This is one particular scale which contributes
        to the data constraints.
    :ivar max_gradient: This element specifies the maximum slope that
        may be used in curves and maps.
    :ivar max_diff: Maximum difference that is permitted between two
        consecutive values if the constraint is applied to an axis.
    :ivar monotony: This specifies the monotony constraints on the data
        object. Note that this applies only to curves and maps.
    :ivar unit_ref: This is the unit to which the physical constraints
        relate to. In particular, it is the physical unit of the
        specified limits.
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
        name = "PHYS-CONSTRS"

    lower_limit: Optional[Limit] = field(
        default=None,
        metadata={
            "name": "LOWER-LIMIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    upper_limit: Optional[Limit] = field(
        default=None,
        metadata={
            "name": "UPPER-LIMIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    scale_constrs: Optional["PhysConstrs.ScaleConstrs"] = field(
        default=None,
        metadata={
            "name": "SCALE-CONSTRS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_gradient: Optional[NumericalValue] = field(
        default=None,
        metadata={
            "name": "MAX-GRADIENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_diff: Optional[NumericalValue] = field(
        default=None,
        metadata={
            "name": "MAX-DIFF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    monotony: Optional[MonotonyEnum] = field(
        default=None,
        metadata={
            "name": "MONOTONY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    unit_ref: Optional["PhysConstrs.UnitRef"] = field(
        default=None,
        metadata={
            "name": "UNIT-REF",
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
    class ScaleConstrs:
        scale_constr: List[ScaleConstr] = field(
            default_factory=list,
            metadata={
                "name": "SCALE-CONSTR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class UnitRef(Ref):
        dest: Optional[UnitSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
