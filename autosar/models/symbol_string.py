from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SymbolString:
    """
    This meta-class has the ability to contain a string plus an additional
    namePattern.

    Please note that this meta-class has only been introduced to fix an
    issue with the backwards compatibility between R4.0.3 and R4.1.1 in the
    context of McDataInstance.

    :ivar value:
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
    :ivar name_pattern: This attribute represents a pattern which shall
        be used to define the value of the identifier if the CIdentifier
        in question is part of a blueprint. For more details refer to
        TPS_StandardizationTemplate.
    """

    class Meta:
        name = "SYMBOL-STRING"

    value: str = field(
        default="",
        metadata={
            "required": True,
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
    name_pattern: str | None = field(
        default=None,
        metadata={
            "name": "NAME-PATTERN",
            "type": "Attribute",
        },
    )
