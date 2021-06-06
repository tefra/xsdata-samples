from dataclasses import dataclass, field
from typing import List, Optional
from .interpolation_routine import InterpolationRoutine
from .ref import Ref
from .sw_record_layout_subtypes_enum import SwRecordLayoutSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class InterpolationRoutineMapping:
    """This meta-class provides a mapping between one record layout and its
    matching interpolation routines.

    This allows to formally specify the semantics of the interpolation
    routines. The use case is such that the curves/Maps define an
    interpolation method. This mapping table specifies which
    interpolation routine implements methods for a particular record
    layout. Using this information, the implementer of a software-
    component can select the appropriate interpolation routine.

    :ivar interpolation_routines: This is one particular interpolation
        routine which is mapped to the record layout.
    :ivar sw_record_layout_ref: This refers to the record layout which
        is mapped to interpolation routines.
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
        name = "INTERPOLATION-ROUTINE-MAPPING"

    interpolation_routines: Optional["InterpolationRoutineMapping.InterpolationRoutines"] = field(
        default=None,
        metadata={
            "name": "INTERPOLATION-ROUTINES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sw_record_layout_ref: Optional["InterpolationRoutineMapping.SwRecordLayoutRef"] = field(
        default=None,
        metadata={
            "name": "SW-RECORD-LAYOUT-REF",
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
    class InterpolationRoutines:
        interpolation_routine: List[InterpolationRoutine] = field(
            default_factory=list,
            metadata={
                "name": "INTERPOLATION-ROUTINE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class SwRecordLayoutRef(Ref):
        dest: Optional[SwRecordLayoutSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
