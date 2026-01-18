from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .admin_data import MlFormula
from .ecuc_condition_formula import EcucConditionFormula
from .ecuc_query import EcucQuery

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EcucConditionSpecification:
    """
    Allows to define existence dependencies based on the value of parameter
    values.

    :ivar condition_formula: Definition of the formula used to define
        existence dependencies.
    :ivar ecuc_querys: Query to the ECU Configuration Description.
    :ivar informal_formula: Informal description of the condition used
        to to define existence dependencies.
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
        name = "ECUC-CONDITION-SPECIFICATION"

    condition_formula: EcucConditionFormula | None = field(
        default=None,
        metadata={
            "name": "CONDITION-FORMULA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ecuc_querys: EcucConditionSpecification.EcucQuerys | None = field(
        default=None,
        metadata={
            "name": "ECUC-QUERYS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    informal_formula: MlFormula | None = field(
        default=None,
        metadata={
            "name": "INFORMAL-FORMULA",
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
    class EcucQuerys:
        ecuc_query: list[EcucQuery] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-QUERY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
