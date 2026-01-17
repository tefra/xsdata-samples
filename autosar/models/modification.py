from dataclasses import dataclass, field
from typing import Optional

from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Modification:
    """
    This meta-class represents the ability to record what has changed in a
    document in comparison to its predecessor.

    :ivar change: This property denotes the one particular change which
        was performed on the object.
    :ivar reason: This property represents the rationale for the
        particular change.
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
        name = "MODIFICATION"

    change: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "CHANGE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    reason: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "REASON",
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
