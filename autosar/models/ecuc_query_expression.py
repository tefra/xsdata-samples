from dataclasses import dataclass, field
from typing import ForwardRef, Optional

from .ecuc_definition_element_subtypes_enum import (
    EcucDefinitionElementSubtypesEnum,
)
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EcucQueryExpression:
    """
    Defines a query expression to the ECUC Description and output the
    result as an numerical value.

    Due to the "mixedString" nature of the formula there can be several
    EcuQueryExpressions used.

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
        name = "ECUC-QUERY-EXPRESSION"

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
                    "name": "CONFIG-ELEMENT-DEF-GLOBAL-REF",
                    "type": ForwardRef(
                        "EcucQueryExpression.ConfigElementDefGlobalRef"
                    ),
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "CONFIG-ELEMENT-DEF-LOCAL-REF",
                    "type": ForwardRef(
                        "EcucQueryExpression.ConfigElementDefLocalRef"
                    ),
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            ),
        },
    )

    @dataclass
    class ConfigElementDefGlobalRef(Ref):
        dest: EcucDefinitionElementSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ConfigElementDefLocalRef(Ref):
        dest: EcucDefinitionElementSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
