from __future__ import annotations

from dataclasses import dataclass, field

from .identifier import Identifier
from .integer import Integer
from .rule_arguments import RuleArguments

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RuleBasedValueSpecification:
    """
    This meta-class is used to support a rule-based initialization approach
    for data types with an array-nature (ApplicationArrayDataType and
    ImplementationDataType of category ARRAY) or a compound
    ApplicationPrimitiveDataType (which also boils down to an
    array-nature).

    :ivar rule: This denotes the name of the rule of the
        RuleBasedValueSpecification. The rule determines the calculation
        specification according which the arguments are used to
        calculated the values.
    :ivar argumentss: This represents the arguments for the
        RuleBasedValueSpecification. The upper multiplicity of this role
        has been increased to * due to resolving an atpVariation
        stereotype. The previous value was 1.
    :ivar max_size_to_fill: If a rule is chosen which does not fill
        until the end, this determines until which size the rule shall
        fill the values.
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
        name = "RULE-BASED-VALUE-SPECIFICATION"

    rule: Identifier | None = field(
        default=None,
        metadata={
            "name": "RULE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    argumentss: RuleBasedValueSpecification.Argumentss | None = field(
        default=None,
        metadata={
            "name": "ARGUMENTSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_size_to_fill: Integer | None = field(
        default=None,
        metadata={
            "name": "MAX-SIZE-TO-FILL",
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
    class Argumentss:
        rule_arguments: list[RuleArguments] = field(
            default_factory=list,
            metadata={
                "name": "RULE-ARGUMENTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
