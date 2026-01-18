from dataclasses import dataclass, field
from typing import Optional

from .l_long_name import LLongName

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class MultilanguageLongName:
    """
    This meta-class represents the ability to specify a long name which
    acts in the role of a headline.

    It is intended for human readers. Per language it should be around max
    80 characters.

    :ivar l_4: This is the long name in one particular language.
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
        name = "MULTILANGUAGE-LONG-NAME"

    l_4: list[LLongName] = field(
        default_factory=list,
        metadata={
            "name": "L-4",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
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
