from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_keyword_2 import TypeKeyword2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class Keyword2(TypeKeyword2):
    """
    Detail information of keywords.

    Parameters
    ----------
    text
        Information for a keyword.
    """

    class Meta:
        name = "Keyword"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    text: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "max_occurs": 999,
        },
    )
