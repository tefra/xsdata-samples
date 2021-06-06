from dataclasses import dataclass, field
from typing import List, Optional
from .br import Br
from .emphasis_text import EmphasisText
from .l_enum_simple import LEnumSimple
from .space_value import SpaceValue
from .tt import Tt
from .xref import Xref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class LVerbatim:
    """MixedContentForVerbatim in one particular language.

    The language is denoted in the attribute l.

    :ivar content:
    :ivar tt: This represents a technical term in verbatim. Note that
        it's the responibility of the user not to take a tt that would
        add additional character to the text (such as SgmlElement).
    :ivar e: This is emphsized text. Note that in verbatim, the
        attribute font should not be considered since verbatim is always
        rendered as monospace font.
    :ivar xref: This is a crossreference within a verbatim text. The
        attributes may disturb the arrangement of the text. It is
        subject to the author to keep this under control.
    :ivar br: This element is the same as function here as in a HTML
        document i.e. it forces a line break.
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
    """
    class Meta:
        name = "L-VERBATIM"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    tt: List[Tt] = field(
        default_factory=list,
        metadata={
            "name": "TT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    e: List[EmphasisText] = field(
        default_factory=list,
        metadata={
            "name": "E",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    xref: List[Xref] = field(
        default_factory=list,
        metadata={
            "name": "XREF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    br: List[Br] = field(
        default_factory=list,
        metadata={
            "name": "BR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
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
    l: Optional[LEnumSimple] = field(
        default=None,
        metadata={
            "name": "L",
            "type": "Attribute",
            "required": True,
        }
    )
    space: Optional[SpaceValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        }
    )
