from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ExtIdClassEnum:
    """This is in fact an enumerator.

    The possible values are all legal XML names of identifiable objects
    even those of other XML files. If the schemas of all questionable
    files are generated from a common meta-model, this is something like
    an IdentifiableSubtypesEnum. Maybe a future version of the Schema
    generator can generate such an enum. As of now it is specified as
    string.

    :ivar value:
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
        name = "EXT-ID-CLASS-ENUM"

    value: Optional[str] = field(
        default=None
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
