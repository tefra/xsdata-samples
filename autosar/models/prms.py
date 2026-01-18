from dataclasses import dataclass, field

from .chapter_enum_break_simple import ChapterEnumBreakSimple
from .general_parameter import GeneralParameter
from .keep_with_previous_enum_simple import KeepWithPreviousEnumSimple
from .multilanguage_long_name import MultilanguageLongName

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Prms:
    """
    This metaclass represents the ability to specify a parameter table.

    It can be used e.g. to specify parameter tables in a data sheet.

    :ivar label: This represents the caption of the parameter table.
    :ivar prm: This represents one particular parameter in the table.
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
        name = "PRMS"

    label: MultilanguageLongName | None = field(
        default=None,
        metadata={
            "name": "LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    prm: list[GeneralParameter] = field(
        default_factory=list,
        metadata={
            "name": "PRM",
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
