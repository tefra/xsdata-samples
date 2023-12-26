from dataclasses import dataclass, field
from typing import Optional
from .align_enum_simple import AlignEnumSimple

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Colspec:
    """
    This meta-class represents the ability to specify the properties of a column in
    a  table.

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
        aligned within the specified column. Default is "LEFT"
    :ivar colname: Specifies the name of the column.
    :ivar colnum: column number (allows to sort the columns).
    :ivar colsep: Indicates whether a line should be displayed right of
        this column in the column specification.
    :ivar colwidth: Width of the column. You can enter absolute values
        such as 4 cm, or relative values marked with * (e.g.,  2* for
        column widths double those of other columns with 1*). The unit
        can be added to the number in the string. Possible units are:
        cm, mm, px, pt.
    :ivar rowsep: Indicates whether a line should be displayed at the
        bottom end of the cells of the column defined in the Colspec.
    """

    class Meta:
        name = "COLSPEC"

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
    align: Optional[AlignEnumSimple] = field(
        default=None,
        metadata={
            "name": "ALIGN",
            "type": "Attribute",
        },
    )
    colname: Optional[str] = field(
        default=None,
        metadata={
            "name": "COLNAME",
            "type": "Attribute",
        },
    )
    colnum: Optional[str] = field(
        default=None,
        metadata={
            "name": "COLNUM",
            "type": "Attribute",
        },
    )
    colsep: Optional[str] = field(
        default=None,
        metadata={
            "name": "COLSEP",
            "type": "Attribute",
            "pattern": r"[0-1]",
        },
    )
    colwidth: Optional[str] = field(
        default=None,
        metadata={
            "name": "COLWIDTH",
            "type": "Attribute",
        },
    )
    rowsep: Optional[str] = field(
        default=None,
        metadata={
            "name": "ROWSEP",
            "type": "Attribute",
            "pattern": r"[0-1]",
        },
    )
