from dataclasses import dataclass, field
from typing import ForwardRef, Optional

from .br import Br
from .emphasis_text import EmphasisText
from .index_entry import IndexEntry
from .l_enum_simple import LEnumSimple
from .ref import Ref
from .supscript import Supscript
from .traceable_subtypes_enum import TraceableSubtypesEnum
from .tt import Tt
from .xref import Xref
from .xref_target import XrefTarget

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SlOverviewParagraph:
    """
    MixedContentForOverviewParagraph in one particular language.

    The language is defined by the context. The attribute l is there only
    for backwards compatibility and shall be ignored.

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
    :ivar l: The attribute l is there only for backwards compatibility
        and shall be ignored.
    :ivar content:
    """

    class Meta:
        name = "SL-OVERVIEW-PARAGRAPH"

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
                    "name": "BR",
                    "type": Br,
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "FT",
                    "type": ForwardRef("SlOverviewParagraph"),
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "TRACE-REF",
                    "type": ForwardRef("SlOverviewParagraph.TraceRef"),
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "TT",
                    "type": Tt,
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
                    "type": ForwardRef("SlOverviewParagraph.Sup"),
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "SUB",
                    "type": ForwardRef("SlOverviewParagraph.Sub"),
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
