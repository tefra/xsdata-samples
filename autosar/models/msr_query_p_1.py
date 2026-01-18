from __future__ import annotations

from dataclasses import dataclass, field

from .chapter_enum_break_simple import ChapterEnumBreakSimple
from .keep_with_previous_enum_simple import KeepWithPreviousEnumSimple
from .msr_query_props import MsrQueryProps
from .topic_content import TopicContent

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class MsrQueryP1:
    """
    This meta-class represents the ability to express a query which yields
    the content of a topic as a result.

    :ivar msr_query_props: This is argument and properties of the
        paragraph query.
    :ivar msr_query_result_p_1: This represents the result of the query.
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
    :ivar si: This attribute allows to denote a semantic information
        which is used to identify documentation objects to be selected
        in customizable document views. It shall be defined in agreement
        between the involved parties.
    :ivar view: This attribute lists the document views in which the
        object shall appear. If it is missing, the object appears in all
        document views.
    :ivar break_value: This attributes allows to specify a forced page
        break.
    :ivar keep_with_previous: This attribute denotes the pagination
        policy. In particular it defines if the containing text block
        shall be kept together with the previous block.
    """

    class Meta:
        name = "MSR-QUERY-P-1"

    msr_query_props: MsrQueryProps | None = field(
        default=None,
        metadata={
            "name": "MSR-QUERY-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    msr_query_result_p_1: TopicContent | None = field(
        default=None,
        metadata={
            "name": "MSR-QUERY-RESULT-P-1",
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
    si: list[str] = field(
        default_factory=list,
        metadata={
            "name": "SI",
            "type": "Attribute",
            "tokens": True,
        },
    )
    view: str | None = field(
        default=None,
        metadata={
            "name": "VIEW",
            "type": "Attribute",
            "pattern": r"(-?[a-zA-Z_]+)(( )+-?[a-zA-Z_]+)*",
        },
    )
    break_value: ChapterEnumBreakSimple | None = field(
        default=None,
        metadata={
            "name": "BREAK",
            "type": "Attribute",
        },
    )
    keep_with_previous: KeepWithPreviousEnumSimple | None = field(
        default=None,
        metadata={
            "name": "KEEP-WITH-PREVIOUS",
            "type": "Attribute",
        },
    )
