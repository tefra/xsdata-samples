from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional

from .br import Br
from .emphasis_text import EmphasisText
from .index_entry import IndexEntry
from .l_enum_simple import LEnumSimple
from .ref import Ref
from .sl_paragraph import SlParagraph
from .std import Std
from .supscript import Supscript
from .traceable_subtypes_enum import TraceableSubtypesEnum
from .tt import Tt
from .xdoc import Xdoc
from .xfile import Xfile
from .xref import Xref
from .xref_target import XrefTarget

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class LParagraph:
    """This is the text for a paragraph in one particular language.

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
    :ivar content:
    """

    class Meta:
        name = "L-PARAGRAPH"

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
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "FT",
                    "type": SlParagraph,
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "TRACE-REF",
                    "type": ForwardRef("LParagraph.TraceRef"),
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "TT",
                    "type": Tt,
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "BR",
                    "type": Br,
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "XREF",
                    "type": Xref,
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "XREF-TARGET",
                    "type": XrefTarget,
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "E",
                    "type": EmphasisText,
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "SUP",
                    "type": ForwardRef("LParagraph.Sup"),
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "SUB",
                    "type": ForwardRef("LParagraph.Sub"),
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "IE",
                    "type": IndexEntry,
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "STD",
                    "type": Std,
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "XDOC",
                    "type": Xdoc,
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "XFILE",
                    "type": Xfile,
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            ),
        },
    )

    @dataclass
    class TraceRef(Ref):
        dest: Optional[TraceableSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class Sub(Supscript):
        pass

    @dataclass
    class Sup(Supscript):
        pass
