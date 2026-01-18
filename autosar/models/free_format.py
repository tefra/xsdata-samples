from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import DocumentationBlock
from .integer import Integer
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class FreeFormat:
    """
    Representing freely defined data.

    :ivar introduction: This represents introductory documentation about
        the schedule table entry.
    :ivar delay: Relative delay between this tableEntry and the start of
        the successor in the schedule table in seconds.
    :ivar position_in_table: Relative position in the schedule table.
        The first entry index in the schedule table is 0.
    :ivar byte_values:
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
        name = "FREE-FORMAT"

    introduction: None | DocumentationBlock = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    delay: None | TimeValue = field(
        default=None,
        metadata={
            "name": "DELAY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    position_in_table: None | Integer = field(
        default=None,
        metadata={
            "name": "POSITION-IN-TABLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    byte_values: None | FreeFormat.ByteValues = field(
        default=None,
        metadata={
            "name": "BYTE-VALUES",
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

    @dataclass(kw_only=True)
    class ByteValues:
        """
        :ivar byte_value: The integer Value of a freely defined data
            byte.
        """

        byte_value: list[Integer] = field(
            default_factory=list,
            metadata={
                "name": "BYTE-VALUE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
                "max_occurs": 8,
            },
        )
