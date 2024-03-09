from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_keyword_5 import TypeKeyword5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class Keyword5(TypeKeyword5):
    """
    Detail information of keywords.

    Parameters
    ----------
    text
        Information for a keyword.
    """

    class Meta:
        name = "Keyword"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    text: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "max_occurs": 999,
        },
    )
