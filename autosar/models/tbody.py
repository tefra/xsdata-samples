from dataclasses import dataclass, field

from .row import Row
from .valign_enum_simple import ValignEnumSimple

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Tbody:
    """
    This meta-class represents a part within a table group.

    Such a part can be the table head, the table body or the table foot.

    :ivar row: This is a particular row in a table. The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
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
    :ivar valign: Indicates how the cells in the rows shall be aligned.
        Default is inherited from tbody, otherwise it is "TOP"
    """

    class Meta:
        name = "TBODY"

    row: list[Row] = field(
        default_factory=list,
        metadata={
            "name": "ROW",
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
    valign: ValignEnumSimple | None = field(
        default=None,
        metadata={
            "name": "VALIGN",
            "type": "Attribute",
        },
    )
