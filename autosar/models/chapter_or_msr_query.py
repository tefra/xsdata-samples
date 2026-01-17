from dataclasses import dataclass, field
from typing import Optional

from .chapter import (
    Chapter,
    MsrQueryChapter,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ChapterOrMsrQuery:
    """
    This meta-class represents the ability to denote a particular chapter
    or a query returning a chapter.

    :ivar chapter: This establishes a subschapter. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was 1.
    :ivar msr_query_chapter: This represents automatically contributed
        chapters provided by an msrquery.
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
        name = "CHAPTER-OR-MSR-QUERY"

    chapter: list[Chapter] = field(
        default_factory=list,
        metadata={
            "name": "CHAPTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    msr_query_chapter: list[MsrQueryChapter] = field(
        default_factory=list,
        metadata={
            "name": "MSR-QUERY-CHAPTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
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
