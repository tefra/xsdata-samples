from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.autosar_operation_argument_instance_subtypes_enum import AutosarOperationArgumentInstanceSubtypesEnum
from autosar.models.autosar_variable_instance_subtypes_enum import AutosarVariableInstanceSubtypesEnum
from autosar.models.ref import Ref
from autosar.models.timing_condition_subtypes_enum import TimingConditionSubtypesEnum
from autosar.models.timing_description_event_subtypes_enum import TimingDescriptionEventSubtypesEnum
from autosar.models.timing_mode_instance_subtypes_enum import TimingModeInstanceSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TimingConditionFormula:
    """A TimingConditionFormula describes a specific dependency.

    The expression shall be a boolean expression addressing modes,
    variables, arguments, and/or events.

    :ivar content:
    :ivar timing_argument_ref: This refers to an argument of an
        operation call.
    :ivar timing_condition_ref: This refers to a timing condition that
        is part of an expression describing the dependency on a specific
        condition.
    :ivar timing_event_ref: This refers to a timing event.
    :ivar timing_mode_ref: This refers to a mode declaration.
    :ivar timing_variable_ref: This refers to a variable.
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
        name = "TIMING-CONDITION-FORMULA"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    timing_argument_ref: List["TimingConditionFormula.TimingArgumentRef"] = field(
        default_factory=list,
        metadata={
            "name": "TIMING-ARGUMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    timing_condition_ref: List["TimingConditionFormula.TimingConditionRef"] = field(
        default_factory=list,
        metadata={
            "name": "TIMING-CONDITION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    timing_event_ref: List["TimingConditionFormula.TimingEventRef"] = field(
        default_factory=list,
        metadata={
            "name": "TIMING-EVENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    timing_mode_ref: List["TimingConditionFormula.TimingModeRef"] = field(
        default_factory=list,
        metadata={
            "name": "TIMING-MODE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    timing_variable_ref: List["TimingConditionFormula.TimingVariableRef"] = field(
        default_factory=list,
        metadata={
            "name": "TIMING-VARIABLE-REF",
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
    class TimingArgumentRef(Ref):
        dest: Optional[AutosarOperationArgumentInstanceSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TimingConditionRef(Ref):
        dest: Optional[TimingConditionSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TimingEventRef(Ref):
        dest: Optional[TimingDescriptionEventSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TimingModeRef(Ref):
        dest: Optional[TimingModeInstanceSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TimingVariableRef(Ref):
        dest: Optional[AutosarVariableInstanceSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
