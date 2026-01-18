from dataclasses import dataclass, field

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RecordLayoutIteratorPoint:
    """
    This meta-class denotes a start / endpoint for the iteration of a
    SwRecordLayoutGroup.

    It can be an integer or one of the keywords MAX-TEXT-SIZE|ARRAY-SIZE.
    Note that negative numbers are counted backwards. Therefore e.g. -1
    refers to the last value.

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
        name = "RECORD-LAYOUT-ITERATOR-POINT"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"-?([0-9]+|MAX-TEXT-SIZE|ARRAY-SIZE)",
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
