from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CIdentifier:
    """
    This datatype represents a string, that follows the rules of C-identifiers.

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
    :ivar blueprint_value: This represents a description that documents
        how the value shall be defined when deriving objects from the
        blueprint.
    :ivar name_pattern: This attribute represents a pattern which shall
        be used to define the value of the identifier if the CIdentifier
        in question is part of a blueprint.   For more details refer to
        TPS_StandardizationTemplate.
    """
    class Meta:
        name = "C-IDENTIFIER"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"[a-zA-Z_][a-zA-Z0-9_]*",
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
    blueprint_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "BLUEPRINT-VALUE",
            "type": "Attribute",
        }
    )
    name_pattern: Optional[str] = field(
        default=None,
        metadata={
            "name": "NAME-PATTERN",
            "type": "Attribute",
        }
    )
