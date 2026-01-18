from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

from .ecuc_query_subtypes_enum import EcucQuerySubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EcucConditionFormula:
    """
    This formula shall yield a boolean expression depending on ecuc
    queries.

    Note that the EcucConditionFormula is a mixed string. Therefore, the
    properties have the upper multiplicity 1.

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
        name = "ECUC-CONDITION-FORMULA"

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
                    "name": "ECUC-QUERY-REF",
                    "type": ForwardRef("EcucConditionFormula.EcucQueryRef"),
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "ECUC-QUERY-STRING-REF",
                    "type": ForwardRef(
                        "EcucConditionFormula.EcucQueryStringRef"
                    ),
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            ),
        },
    )

    @dataclass
    class EcucQueryRef(Ref):
        dest: EcucQuerySubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class EcucQueryStringRef(Ref):
        dest: EcucQuerySubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
