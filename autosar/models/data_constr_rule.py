from dataclasses import dataclass, field
from typing import Optional
from .integer import Integer
from .internal_constrs import InternalConstrs
from .phys_constrs import PhysConstrs

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DataConstrRule:
    """
    This meta-class represents the ability to express one specific data constraint
    rule.

    :ivar constr_level: This attribute describes the category of a
        constraint. One of its functions is in the area of constraint
        violation, where it can be used from a certain level, to produce
        error messages. The lower the level, the more stringent the
        check. Used to distinguish hard or soft limits.
    :ivar phys_constrs: Describes the limitations applicable on the
        physical domain (as opposed to the internal domain).
    :ivar internal_constrs: Describes the limitations applicable on the
        internal domain (as opposed to the physical domain).
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
        name = "DATA-CONSTR-RULE"

    constr_level: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "CONSTR-LEVEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    phys_constrs: Optional[PhysConstrs] = field(
        default=None,
        metadata={
            "name": "PHYS-CONSTRS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    internal_constrs: Optional[InternalConstrs] = field(
        default=None,
        metadata={
            "name": "INTERNAL-CONSTRS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )
