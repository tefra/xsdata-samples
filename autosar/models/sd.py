from dataclasses import dataclass, field
from typing import Optional
from .space_value import SpaceValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Sd:
    """
    This class represents a primitive element in a special data group.

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
    :ivar gid: This attributes specifies an identifier. Gid comes from
        the SGML/XML-Term "Generic Identifier" which is the element name
        in XML. The role of this attribute is the same as the name of an
        XML - element.
    :ivar space: This attribute is used to signal an intention that in
        that element, white space should be preserved by applications.
        It is defined according to xml:space as declared by W3C.
    """
    class Meta:
        name = "SD"

    value: Optional[str] = field(
        default=None,
        metadata={
            "white_space": "preserve",
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
    gid: Optional[str] = field(
        default=None,
        metadata={
            "name": "GID",
            "type": "Attribute",
        }
    )
    space: SpaceValue = field(
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
