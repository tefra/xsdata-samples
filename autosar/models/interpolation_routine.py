from dataclasses import dataclass, field
from typing import Optional
from .boolean import Boolean
from .bsw_module_entry_subtypes_enum import BswModuleEntrySubtypesEnum
from .identifier import Identifier
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class InterpolationRoutine:
    """
    This represents an interpolation routine taken to evaluate the contents of a
    curve or map against a specific input value.

    :ivar short_label: This is the name of the interpolation method
        which is implemented by the referenced bswModuleEntry. It
        corresponds to swInterpolationMethod in SwDataDefProps.
    :ivar is_default: This attribute specifies whether the enclosing
        InterpolationRoutine is considered the default in the context
        (defined by the System Template) of a given collection
        InterpolationRoutineMapping that owns the enclosing
        InterpolationRoutine.
    :ivar interpolation_routine_ref: This specifies a BswModuleEntry
        which implements the current interpolation method for the given
        record layout.
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
        name = "INTERPOLATION-ROUTINE"

    short_label: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    is_default: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "IS-DEFAULT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    interpolation_routine_ref: Optional["InterpolationRoutine.InterpolationRoutineRef"] = field(
        default=None,
        metadata={
            "name": "INTERPOLATION-ROUTINE-REF",
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
    class InterpolationRoutineRef(Ref):
        dest: Optional[BswModuleEntrySubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
