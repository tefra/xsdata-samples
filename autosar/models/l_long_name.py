from dataclasses import dataclass, field
from typing import ForwardRef, Optional

from .emphasis_text import EmphasisText
from .index_entry import IndexEntry
from .l_enum_simple import LEnumSimple
from .supscript import Supscript
from .tt import Tt

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class LLongName:
    """
    MixedContentForLongNames in one particular language.

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
    :ivar blueprint_value: This represents a description that documents
        how the value shall be defined when deriving objects from the
        blueprint.
    :ivar content:
    """

    class Meta:
        name = "L-LONG-NAME"

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
    blueprint_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "BLUEPRINT-VALUE",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "TT",
                    "type": Tt,
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "E",
                    "type": EmphasisText,
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "SUP",
                    "type": ForwardRef("LLongName.Sup"),
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "SUB",
                    "type": ForwardRef("LLongName.Sub"),
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "IE",
                    "type": IndexEntry,
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            ),
        },
    )

    @dataclass
    class Sup(Supscript):
        pass

    @dataclass
    class Sub(Supscript):
        pass
