from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.emphasis_text import EmphasisText
from autosar.models.index_entry import IndexEntry
from autosar.models.supscript import Supscript
from autosar.models.tt import Tt

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SingleLanguageLongName:
    """
    SingleLanguageLongName.

    :ivar content:
    :ivar tt: This is a technical term.
    :ivar e: This is emphasized text
    :ivar sup: This is superscript text.
    :ivar sub: This is subscript text.
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
    """
    class Meta:
        name = "SINGLE-LANGUAGE-LONG-NAME"

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
