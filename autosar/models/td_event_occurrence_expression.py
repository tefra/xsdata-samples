from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.autosar_operation_argument_instance import AutosarOperationArgumentInstance
from autosar.models.autosar_variable_instance import AutosarVariableInstance
from autosar.models.td_event_occurrence_expression_formula import TdEventOccurrenceExpressionFormula
from autosar.models.timing_mode_instance import TimingModeInstance

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TdEventOccurrenceExpression:
    """This is used to specify a filter on the occurrences of
    TimingDescriptionEvents by means of a TDEventOccurrenceExpressionFormula.

    Filter criteria can be variable and argument values, i.e. the timing
    event only occurs for specific values, as well as the temporal
    characteristics of the occurrences of arbitrary timing events.

    :ivar arguments: An occurrence expression can reference an arbitrary
        number of OperationArgumentPrototypes in its expression. This
        association aggregates instance references to
        OperationArgumentPrototypes which can be referenced in the
        expression.
    :ivar formula: This is the expression formula which is used to
        describe the occurrence expression.
    :ivar modes: An occurrence expression can reference an arbitrary
        number of TimingModeInstances in its expression. This
        association aggregates instance references to ModeDeclaration
        which can be referenced in the expression.
    :ivar variables: An occurrence expression can reference an arbitrary
        number of VariableDataPrototpyes in its expression. This
        association aggregates instance references to
        VariableDataPrototypes which can be referenced in the
        expression.
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
        name = "TD-EVENT-OCCURRENCE-EXPRESSION"

    arguments: Optional["TdEventOccurrenceExpression.Arguments"] = field(
        default=None,
        metadata={
            "name": "ARGUMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    formula: Optional[TdEventOccurrenceExpressionFormula] = field(
        default=None,
        metadata={
            "name": "FORMULA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    modes: Optional["TdEventOccurrenceExpression.Modes"] = field(
        default=None,
        metadata={
            "name": "MODES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variables: Optional["TdEventOccurrenceExpression.Variables"] = field(
        default=None,
        metadata={
            "name": "VARIABLES",
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
    class Arguments:
        autosar_operation_argument_instance: List[AutosarOperationArgumentInstance] = field(
            default_factory=list,
            metadata={
                "name": "AUTOSAR-OPERATION-ARGUMENT-INSTANCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class Modes:
        timing_mode_instance: List[TimingModeInstance] = field(
            default_factory=list,
            metadata={
                "name": "TIMING-MODE-INSTANCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class Variables:
        autosar_variable_instance: List[AutosarVariableInstance] = field(
            default_factory=list,
            metadata={
                "name": "AUTOSAR-VARIABLE-INSTANCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
