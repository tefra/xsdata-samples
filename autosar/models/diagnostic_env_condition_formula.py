from __future__ import annotations

from dataclasses import dataclass, field

from .diagnostic_env_data_condition import DiagnosticEnvDataCondition
from .diagnostic_env_mode_condition import DiagnosticEnvModeCondition
from .diagnostic_logical_operator_enum import DiagnosticLogicalOperatorEnum
from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiagnosticEnvConditionFormula:
    """
    A DiagnosticEnvConditionFormula embodies the computation instruction
    that is to be evaluated at runtime to determine if the
    DiagnosticEnvironmentalCondition is currently present (i.e. the formula
    is evaluated to true) or not (otherwise).

    The formula itself consists of parts which are combined by the logical
    operations specified by DiagnosticEnvConditionFormula.op. If a
    diagnostic functionality cannot be executed because an environmental
    condition fails then the diagnostic stack shall send a negative
    response code (NRC) back to the client. The value of the NRC is
    directly related to the specific formula and is therefore formalized in
    the attribute DiagnosticEnvConditionFormula.nrcValue.

    :ivar nrc_value: This attribute represents the concrete NRC value
        that shall be returned if the condition fails.
    :ivar op: This attribute represents the concrete operator (supported
        operators: and, or) of the condition formula.
    :ivar parts: This aggregation represents the collection of formula
        parts that can be combined by logical operators.
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
        name = "DIAGNOSTIC-ENV-CONDITION-FORMULA"

    nrc_value: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "NRC-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    op: DiagnosticLogicalOperatorEnum | None = field(
        default=None,
        metadata={
            "name": "OP",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    parts: DiagnosticEnvConditionFormula.Parts | None = field(
        default=None,
        metadata={
            "name": "PARTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
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

    @dataclass
    class Parts:
        diagnostic_env_condition_formula: list[
            DiagnosticEnvConditionFormula
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-ENV-CONDITION-FORMULA",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        diagnostic_env_data_condition: list[DiagnosticEnvDataCondition] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-ENV-DATA-CONDITION",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        diagnostic_env_mode_condition: list[DiagnosticEnvModeCondition] = (
            field(
                default_factory=list,
                metadata={
                    "name": "DIAGNOSTIC-ENV-MODE-CONDITION",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
