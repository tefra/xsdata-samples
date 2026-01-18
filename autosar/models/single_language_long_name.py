from dataclasses import dataclass, field
from typing import ForwardRef, Optional

from .emphasis_text import EmphasisText
from .index_entry import IndexEntry
from .supscript import Supscript
from .tt import Tt

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SingleLanguageLongName:
    """
    SingleLanguageLongName.

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
    :ivar content:
    """

    class Meta:
        name = "SINGLE-LANGUAGE-LONG-NAME"

    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
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
                    "type": ForwardRef("SingleLanguageLongName.Sup"),
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "SUB",
                    "type": ForwardRef("SingleLanguageLongName.Sub"),
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
