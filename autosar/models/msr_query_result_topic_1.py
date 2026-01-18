from __future__ import annotations

from dataclasses import dataclass, field

from .topic_1 import Topic1

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class MsrQueryResultTopic1:
    """
    This metaclass represents the ability to express the result of a query
    which is a set of topics.

    :ivar topic_1: This represents one particular topic in the query
        result.
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
        name = "MSR-QUERY-RESULT-TOPIC-1"

    topic_1: list[Topic1] = field(
        default_factory=list,
        metadata={
            "name": "TOPIC-1",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
