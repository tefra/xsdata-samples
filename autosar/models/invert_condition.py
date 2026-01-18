from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .aggregation_condition import AggregationCondition
from .primitive_attribute_condition import PrimitiveAttributeCondition
from .reference_condition import ReferenceCondition
from .textual_condition import TextualCondition

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class InvertCondition:
    """
    inverts the nested condition.

    :ivar condition: The inverted condition
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
        name = "INVERT-CONDITION"

    condition: InvertCondition.Condition | None = field(
        default=None,
        metadata={
            "name": "CONDITION",
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
    class Condition:
        aggregation_condition: AggregationCondition | None = field(
            default=None,
            metadata={
                "name": "AGGREGATION-CONDITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        invert_condition: InvertCondition | None = field(
            default=None,
            metadata={
                "name": "INVERT-CONDITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        primitive_attribute_condition: PrimitiveAttributeCondition | None = field(
            default=None,
            metadata={
                "name": "PRIMITIVE-ATTRIBUTE-CONDITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        reference_condition: ReferenceCondition | None = field(
            default=None,
            metadata={
                "name": "REFERENCE-CONDITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        textual_condition: TextualCondition | None = field(
            default=None,
            metadata={
                "name": "TEXTUAL-CONDITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
