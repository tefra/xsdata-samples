from dataclasses import dataclass, field
from typing import List, Optional
from .concrete_class_tailoring import (
    AbstractClassTailoring,
    ConcreteClassTailoring,
)
from .constraint_tailoring import ConstraintTailoring

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DataFormatTailoring:
    """
    This class collects all rules that tailor the AUTOSAR templates for a specific
    data exchange point.

    :ivar class_tailorings: Specification of tailorings of Meta Classes
    :ivar constraint_tailorings: Specification of tailorings of
        Constraints that are not explicitly owned by any Meta-Class
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
        name = "DATA-FORMAT-TAILORING"

    class_tailorings: Optional["DataFormatTailoring.ClassTailorings"] = field(
        default=None,
        metadata={
            "name": "CLASS-TAILORINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    constraint_tailorings: Optional["DataFormatTailoring.ConstraintTailorings"] = field(
        default=None,
        metadata={
            "name": "CONSTRAINT-TAILORINGS",
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

    @dataclass
    class ClassTailorings:
        abstract_class_tailoring: List[AbstractClassTailoring] = field(
            default_factory=list,
            metadata={
                "name": "ABSTRACT-CLASS-TAILORING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        concrete_class_tailoring: List[ConcreteClassTailoring] = field(
            default_factory=list,
            metadata={
                "name": "CONCRETE-CLASS-TAILORING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class ConstraintTailorings:
        constraint_tailoring: List[ConstraintTailoring] = field(
            default_factory=list,
            metadata={
                "name": "CONSTRAINT-TAILORING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
