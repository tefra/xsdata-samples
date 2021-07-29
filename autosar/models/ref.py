from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Ref:
    """This primitive denotes a name based reference. For detailed syntax see
    the xsd.pattern.

    * first slash (relative or absolute reference) [optional]
    * Identifier  [required]
    * a sequence of slashes and Identifiers [optional]
    This primitive is used by the meta-model tools to create the references.

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
    :ivar base: This attribute reflects the base to be used for this
        reference.
    :ivar blueprint_value: This represents a description that documents
        how the value shall be defined when deriving objects from the
        blueprint.
    :ivar index: This attribute supports the use case to point on
        specific elements in an array. This is in particular required if
        arrays are used to implement particular data objects.
    """
    class Meta:
        name = "REF"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"/?[a-zA-Z][a-zA-Z0-9_]{0,127}(/[a-zA-Z][a-zA-Z0-9_]{0,127})*",
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
    base: Optional[str] = field(
        default=None,
        metadata={
            "name": "BASE",
            "type": "Attribute",
            "max_length": 128,
            "pattern": r"[a-zA-Z][a-zA-Z0-9_]*",
        }
    )
    blueprint_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "BLUEPRINT-VALUE",
            "type": "Attribute",
        }
    )
    index: Optional[str] = field(
        default=None,
        metadata={
            "name": "INDEX",
            "type": "Attribute",
            "pattern": r"0|[\+]?[1-9][0-9]*|0[xX][0-9a-fA-F]+|0[bB][0-1]+|0[0-7]+",
        }
    )
