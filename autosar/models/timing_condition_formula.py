from dataclasses import dataclass, field
from typing import ForwardRef, Optional

from .autosar_operation_argument_instance_subtypes_enum import (
    AutosarOperationArgumentInstanceSubtypesEnum,
)
from .autosar_variable_instance_subtypes_enum import (
    AutosarVariableInstanceSubtypesEnum,
)
from .ref import Ref
from .timing_condition_subtypes_enum import TimingConditionSubtypesEnum
from .timing_description_event_subtypes_enum import (
    TimingDescriptionEventSubtypesEnum,
)
from .timing_mode_instance_subtypes_enum import TimingModeInstanceSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TimingConditionFormula:
    """
    A TimingConditionFormula describes a specific dependency.

    The expression shall be a boolean expression addressing modes,
    variables, arguments, and/or events.

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
    :ivar content:
    """

    class Meta:
        name = "TIMING-CONDITION-FORMULA"

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
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "TIMING-ARGUMENT-REF",
                    "type": ForwardRef(
                        "TimingConditionFormula.TimingArgumentRef"
                    ),
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "TIMING-CONDITION-REF",
                    "type": ForwardRef(
                        "TimingConditionFormula.TimingConditionRef"
                    ),
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "TIMING-EVENT-REF",
                    "type": ForwardRef(
                        "TimingConditionFormula.TimingEventRef"
                    ),
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "TIMING-MODE-REF",
                    "type": ForwardRef("TimingConditionFormula.TimingModeRef"),
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "TIMING-VARIABLE-REF",
                    "type": ForwardRef(
                        "TimingConditionFormula.TimingVariableRef"
                    ),
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            ),
        },
    )

    @dataclass
    class TimingArgumentRef(Ref):
        dest: AutosarOperationArgumentInstanceSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TimingConditionRef(Ref):
        dest: TimingConditionSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TimingEventRef(Ref):
        dest: TimingDescriptionEventSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TimingModeRef(Ref):
        dest: TimingModeInstanceSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TimingVariableRef(Ref):
        dest: AutosarVariableInstanceSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
