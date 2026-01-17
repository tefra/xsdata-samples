from dataclasses import dataclass, field
from typing import Optional

from .msr_query_topic_1 import MsrQueryTopic1
from .topic_1 import Topic1

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TopicOrMsrQuery:
    """
    This class provides the alternative of a Topic with an MsrQuery which
    delivers a topic.

    :ivar topic_1: This is used to create particcular topics within a
        chapter. A topic is similar to a subchapter, but cannot be
        nesxted and will not appear in the table of contents of the
        document. The upper multiplicity of this role has been increased
        to * due to resolving an atpVariation stereotype. The previous
        value was 1.
    :ivar msr_query_topic_1: This represents automatically contributed
        topics provided by an msrquery.
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
        name = "TOPIC-OR-MSR-QUERY"

    topic_1: list[Topic1] = field(
        default_factory=list,
        metadata={
            "name": "TOPIC-1",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    msr_query_topic_1: list[MsrQueryTopic1] = field(
        default_factory=list,
        metadata={
            "name": "MSR-QUERY-TOPIC-1",
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
