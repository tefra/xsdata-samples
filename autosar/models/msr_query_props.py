from dataclasses import dataclass, field
from typing import Optional

from .msr_query_arg import MsrQueryArg
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class MsrQueryProps:
    """
    This metaclass represents the ability to specificy a query which yields
    some documentation text.

    The qualities of the result are determined by the context in which the
    query is used.

    :ivar msr_query_name: This element specifies the name of the MSR-
        QUERY triggered.
    :ivar msr_query_arg: This element specifies an argument within an
        MsrQuery.
    :ivar comment: This element contains a commentary in text form.
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
        name = "MSR-QUERY-PROPS"

    msr_query_name: String | None = field(
        default=None,
        metadata={
            "name": "MSR-QUERY-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    msr_query_arg: list[MsrQueryArg] = field(
        default_factory=list,
        metadata={
            "name": "MSR-QUERY-ARG",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    comment: String | None = field(
        default=None,
        metadata={
            "name": "COMMENT",
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
