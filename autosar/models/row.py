from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import VariationPoint
from .chapter_enum_break_simple import ChapterEnumBreakSimple
from .entry import Entry
from .keep_with_previous_enum_simple import KeepWithPreviousEnumSimple
from .valign_enum_simple import ValignEnumSimple

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Row:
    """
    This meta-class represents the ability to express one row in a table.

    :ivar entry: This represents one particular table cell. It is an
        entry in the table.
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
    :ivar rowsep: Indicates if by default a line should be displayed
        below the row.
    :ivar valign: Indicates how the cells in the rows shall be aligned.
        Default is inherited from tbody, otherwise it is "TOP"
    """
    class Meta:
        name = "ROW"

    entry: List[Entry] = field(
        default_factory=list,
        metadata={
            "name": "ENTRY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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
    si: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SI",
            "type": "Attribute",
            "tokens": True,
        }
    )
    view: Optional[str] = field(
        default=None,
        metadata={
            "name": "VIEW",
            "type": "Attribute",
            "pattern": r"(-?[a-zA-Z_]+)(( )+-?[a-zA-Z_]+)*",
        }
    )
    break_value: Optional[ChapterEnumBreakSimple] = field(
        default=None,
        metadata={
            "name": "BREAK",
            "type": "Attribute",
        }
    )
    keep_with_previous: Optional[KeepWithPreviousEnumSimple] = field(
        default=None,
        metadata={
            "name": "KEEP-WITH-PREVIOUS",
            "type": "Attribute",
        }
    )
    rowsep: Optional[str] = field(
        default=None,
        metadata={
            "name": "ROWSEP",
            "type": "Attribute",
            "pattern": r"[0-1]",
        }
    )
    valign: Optional[ValignEnumSimple] = field(
        default=None,
        metadata={
            "name": "VALIGN",
            "type": "Attribute",
        }
    )
