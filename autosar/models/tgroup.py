from dataclasses import dataclass, field

from .align_enum_simple import AlignEnumSimple
from .colspec import Colspec
from .tbody import Tbody

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Tgroup:
    """
    This meta-class represents the ability to denote a table section.

    :ivar colspec: This specifies one particular column specification in
        the table. There shall be one entry for each column.
    :ivar thead: This represents the heading of the table section. The
        heading is usually repeated at the beginning of each new page.
    :ivar tfoot: This represents the footer of the table segement. This
        segment is printed at the end of the table or before a page
        break.
    :ivar tbody: This is the main part of the table segment, called the
        table body.
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
    :ivar align: Specifies how the cell entries shall be horizontally
        aligned within the specified TGROUP. Default is "LEFT"
    :ivar cols: This attribute represents the number of columns in the
        table.
    :ivar colsep: Indicates if by default a line shall be drawn between
        the columns of this table group.
    :ivar rowsep: Indicates if by default a line shall be drawn at the
        bottom of the rows in this table group.
    """

    class Meta:
        name = "TGROUP"

    colspec: list[Colspec] = field(
        default_factory=list,
        metadata={
            "name": "COLSPEC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    thead: Tbody | None = field(
        default=None,
        metadata={
            "name": "THEAD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tfoot: Tbody | None = field(
        default=None,
        metadata={
            "name": "TFOOT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tbody: Tbody | None = field(
        default=None,
        metadata={
            "name": "TBODY",
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
    align: AlignEnumSimple | None = field(
        default=None,
        metadata={
            "name": "ALIGN",
            "type": "Attribute",
        },
    )
    cols: str | None = field(
        default=None,
        metadata={
            "name": "COLS",
            "type": "Attribute",
            "pattern": r"0|[\+\-]?[1-9][0-9]*|0[xX][0-9a-fA-F]+|0[bB][0-1]+|0[0-7]+",
        },
    )
    colsep: str | None = field(
        default=None,
        metadata={
            "name": "COLSEP",
            "type": "Attribute",
            "pattern": r"[0-1]",
        },
    )
    rowsep: str | None = field(
        default=None,
        metadata={
            "name": "ROWSEP",
            "type": "Attribute",
            "pattern": r"[0-1]",
        },
    )
