from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.br import Br
from autosar.models.emphasis_text import EmphasisText
from autosar.models.index_entry import IndexEntry
from autosar.models.l_enum_simple import LEnumSimple
from autosar.models.ref import Ref
from autosar.models.sl_overview_paragraph import SlOverviewParagraph
from autosar.models.supscript import Supscript
from autosar.models.traceable_subtypes_enum import TraceableSubtypesEnum
from autosar.models.tt import Tt
from autosar.models.xref import Xref
from autosar.models.xref_target import XrefTarget

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class LOverviewParagraph:
    """MixedContentForOverviewParagraph in one particular language.

    The language is denoted in the attribute l.

    :ivar content:
    :ivar br: This element is the same as function here as in a HTML
        document i.e. it forces a line break.
    :ivar ft: This is a foot note within a paragraph.
    :ivar trace_ref: This allows to place an arbitrary reference to a
        traceable object in documentation.
    :ivar tt: This is a technical term.
    :ivar xref: This is a cross reference.
    :ivar xref_target: This element specifies a reference target which
        can be scattered throughout the text.
    :ivar e: This is emphasis text.
    :ivar sup: This is subscript text.
    :ivar sub: This is superscript text.
    :ivar ie: This is an index entry.
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
        neutral.  It follows ISO 639-1:2002 and is specified in upper
        case.
    :ivar blueprint_value: This represents a description that documents
        how the value shall be defined when deriving objects from the
        blueprint.
    """
    class Meta:
        name = "L-OVERVIEW-PARAGRAPH"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
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
    ft: List[SlOverviewParagraph] = field(
        default_factory=list,
        metadata={
            "name": "FT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    trace_ref: List["LOverviewParagraph.TraceRef"] = field(
        default_factory=list,
        metadata={
            "name": "TRACE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
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
    xref: List[Xref] = field(
        default_factory=list,
        metadata={
            "name": "XREF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    xref_target: List[XrefTarget] = field(
        default_factory=list,
        metadata={
            "name": "XREF-TARGET",
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
    sup: List[Supscript] = field(
        default_factory=list,
        metadata={
            "name": "SUP",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sub: List[Supscript] = field(
        default_factory=list,
        metadata={
            "name": "SUB",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    ie: List[IndexEntry] = field(
        default_factory=list,
        metadata={
            "name": "IE",
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
    blueprint_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "BLUEPRINT-VALUE",
            "type": "Attribute",
        }
    )

    @dataclass
    class TraceRef(Ref):
        dest: Optional[TraceableSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
