from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.coding_text_format_type import CodingTextFormatType
from sdmx_ml.models.level_base_type import LevelBaseType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class LevelType(LevelBaseType):
    """
    LevelType describes a level in a hierarchical codelist.

    Where level is defined as a group where codes can be characterised by
    homogeneous coding, and where the parent of each code in the group is
    at the same higher level of the hierarchy.

    :ivar coding_format: CodingFormat specifies the text formatting of
        the codes in this level. This includes facets such as the
        expected characters and the length of the codes.
    :ivar level: Level describes the next level down in the hierarchy.
    """

    coding_format: CodingTextFormatType | None = field(
        default=None,
        metadata={
            "name": "CodingFormat",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    level: LevelType | None = field(
        default=None,
        metadata={
            "name": "Level",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
