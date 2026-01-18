from dataclasses import dataclass, field

from .graphic import Graphic
from .l_enum_simple import LEnumSimple
from .map import Map

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class LGraphic:
    """
    This meta-class represents the figure in one particular language.

    :ivar graphic: Reference to the actual graphic represented in the
        figure.
    :ivar map: Image maps enable authors to specify regions of an image
        or object and assign a specific action to each region.
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
    """

    class Meta:
        name = "L-GRAPHIC"

    graphic: Graphic | None = field(
        default=None,
        metadata={
            "name": "GRAPHIC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    map: Map | None = field(
        default=None,
        metadata={
            "name": "MAP",
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
    l: LEnumSimple | None = field(
        default=None,
        metadata={
            "name": "L",
            "type": "Attribute",
            "required": True,
        },
    )
