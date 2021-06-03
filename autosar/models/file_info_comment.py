from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import Sdg

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class FileInfoComment:
    """
    This class supports StructuredComment to provide auxiliary information with
    the goal to create a comment.

    :ivar sdgs: This property allows to keep special data which is not
        represented by the standard model. It can be utilized to keep
        e.g. tool specific data.
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
        name = "FILE-INFO-COMMENT"

    sdgs: Optional["FileInfoComment.Sdgs"] = field(
        default=None,
        metadata={
            "name": "SDGS",
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

    @dataclass
    class Sdgs:
        sdg: List[Sdg] = field(
            default_factory=list,
            metadata={
                "name": "SDG",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
