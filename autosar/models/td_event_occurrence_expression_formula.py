from dataclasses import dataclass, field
from typing import List, Optional
from .autosar_operation_argument_instance_subtypes_enum import AutosarOperationArgumentInstanceSubtypesEnum
from .autosar_variable_instance_subtypes_enum import AutosarVariableInstanceSubtypesEnum
from .ref import Ref
from .timing_description_event_subtypes_enum import TimingDescriptionEventSubtypesEnum
from .timing_mode_instance_subtypes_enum import TimingModeInstanceSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TdEventOccurrenceExpressionFormula:
    """This is an extension of the FormulaExpression for the AUTOSAR Timing
    Extensions.

    A TDEventOccurrenceExpressionFormula provides the means to express
    the temporal characteristics of timing event occurrences in
    correlation with specific variable and argument values. The formal
    definition of the extended functions (ExtUnaryFunctions) is
    described in detail in the AUTOSAR Timing Extensions.

    :ivar content:
    :ivar argument_ref: This is one particular argument value used in
        the expression formula.
    :ivar event_ref: This is one particular timing description event
        used in the expression formula.
    :ivar mode_ref: This is one particular mode used in the expression
        formula.
    :ivar variable_ref: This is one particular variable value used in
        the expression formula.
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
        name = "TD-EVENT-OCCURRENCE-EXPRESSION-FORMULA"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    argument_ref: List["TdEventOccurrenceExpressionFormula.ArgumentRef"] = field(
        default_factory=list,
        metadata={
            "name": "ARGUMENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    event_ref: List["TdEventOccurrenceExpressionFormula.EventRef"] = field(
        default_factory=list,
        metadata={
            "name": "EVENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    mode_ref: List["TdEventOccurrenceExpressionFormula.ModeRef"] = field(
        default_factory=list,
        metadata={
            "name": "MODE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variable_ref: List["TdEventOccurrenceExpressionFormula.VariableRef"] = field(
        default_factory=list,
        metadata={
            "name": "VARIABLE-REF",
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
    class ArgumentRef(Ref):
        dest: Optional[AutosarOperationArgumentInstanceSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class EventRef(Ref):
        dest: Optional[TimingDescriptionEventSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ModeRef(Ref):
        dest: Optional[TimingModeInstanceSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class VariableRef(Ref):
        dest: Optional[AutosarVariableInstanceSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
