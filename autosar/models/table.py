from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .caption import Caption
from .chapter_enum_break_simple import ChapterEnumBreakSimple
from .float_enum_simple import FloatEnumSimple
from .frame_enum_simple import FrameEnumSimple
from .keep_with_previous_enum_simple import KeepWithPreviousEnumSimple
from .orient_enum_simple import OrientEnumSimple
from .tgroup import Tgroup

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Table:
    """
    This class implements an exchange table according to OASIS Technical
    Resolution TR 9503:1995. http://www.oasis-open.org/specs/a503.htm.

    :ivar table_caption: This element specifies the table heading.
    :ivar tgroup: A table can be built of individual segments. Such a
        segment is called tgroup.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
    :ivar colsep: Indicates if by default a line should be drawn between
        the columns of this table.
    :ivar float_value: Indicate whether it is allowed to break the
        element.
    :ivar frame: Used to defined the frame line around a table.
    :ivar help_entry: This specifies an entry point in an online help
        system to be linked with the parent class. The syntax shall be
        defined by the applied help system respectively help system
        generator.
    :ivar orient: Indicate whether a table should be represented as
        landscape or portrait. * land : landscape * port : portrait
    :ivar pgwide: Used to indicate wether the figure should take the
        complete page width (value = "pgwide") or not (value =
        "noPgwide").
    :ivar rowsep: Indicates if by default  a line should be drawn at the
        bottom of table rows.
    :ivar tabstyle: Indicates an external table style.
    """

    class Meta:
        name = "TABLE"

    table_caption: Caption | None = field(
        default=None,
        metadata={
            "name": "TABLE-CAPTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tgroup: list[Tgroup] = field(
        default_factory=list,
        metadata={
            "name": "TGROUP",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: VariationPoint | None = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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
    colsep: str | None = field(
        default=None,
        metadata={
            "name": "COLSEP",
            "type": "Attribute",
            "pattern": r"[0-1]",
        },
    )
    float_value: FloatEnumSimple | None = field(
        default=None,
        metadata={
            "name": "FLOAT",
            "type": "Attribute",
        },
    )
    frame: FrameEnumSimple | None = field(
        default=None,
        metadata={
            "name": "FRAME",
            "type": "Attribute",
        },
    )
    help_entry: str | None = field(
        default=None,
        metadata={
            "name": "HELP-ENTRY",
            "type": "Attribute",
        },
    )
    orient: OrientEnumSimple | None = field(
        default=None,
        metadata={
            "name": "ORIENT",
            "type": "Attribute",
        },
    )
    pgwide: str | None = field(
        default=None,
        metadata={
            "name": "PGWIDE",
            "type": "Attribute",
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
    tabstyle: str | None = field(
        default=None,
        metadata={
            "name": "TABSTYLE",
            "type": "Attribute",
        },
    )
