from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ForeignModelReference:
    """This meta-class represents the ability to express a late binding
    reference to a foreign model element.

    The foreign model element can be from every model. Even if it is
    modeled according to the association representation, it is not
    limited to refer to AUTOSAR model elements.

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
    :ivar base: This establishes the reference base.
    :ivar dest: This attribute represents the class of the referenced
        model element. It is a String, since the model element can be in
        any model. Therefore we cannot have any assumption here.
    """
    class Meta:
        name = "FOREIGN-MODEL-REFERENCE"

    value: Optional[str] = field(
        default=None,
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
        }
    )
    dest: Optional[str] = field(
        default=None,
        metadata={
            "name": "DEST",
            "type": "Attribute",
        }
    )
