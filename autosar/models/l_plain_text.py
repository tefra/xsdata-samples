from dataclasses import dataclass, field
from typing import List, Optional
from .l_enum_simple import LEnumSimple
from .space_value import SpaceValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class LPlainText:
    """This represents plain string in one particular language.

    The language is denoted in the attribute l.

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
    :ivar l: 'This attribute denotes the language in which the language
        specific document entity is given. Note that "FOR-ALL" means,
        that the entity is applicable to all languages. It is language
        neutral. It follows ISO 639-1:2002 and is specified in upper
        case.
    :ivar space: This attribute is used to signal an intention that in
        that element, white space should be preserved by applications.
        It is defined according to xml:space as declared by W3C.
    :ivar content:
    """

    class Meta:
        name = "L-PLAIN-TEXT"

    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    l: Optional[LEnumSimple] = field(
        default=None,
        metadata={
            "name": "L",
            "type": "Attribute",
            "required": True,
        },
    )
    space: SpaceValue = field(
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
