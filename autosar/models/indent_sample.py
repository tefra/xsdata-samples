from __future__ import annotations

from dataclasses import dataclass, field

from .item_label_pos_enum_simple import ItemLabelPosEnumSimple
from .l_overview_paragraph import LOverviewParagraph

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class IndentSample:
    """
    This represents the ability to specify indentation of a labeled list by
    providing a sample content.

    This content can be measured by the rendering system in order to
    determine the width of indentation.

    :ivar l_2: This represents the indent sample in one particular
        language.
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
    :ivar item_label_pos: The position of the label in case the label is
        too long. The default is  "NO-NEWLINE"
    """

    class Meta:
        name = "INDENT-SAMPLE"

    l_2: list[LOverviewParagraph] = field(
        default_factory=list,
        metadata={
            "name": "L-2",
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
    item_label_pos: None | ItemLabelPosEnumSimple = field(
        default=None,
        metadata={
            "name": "ITEM-LABEL-POS",
            "type": "Attribute",
        },
    )
