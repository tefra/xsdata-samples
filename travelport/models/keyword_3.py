from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_keyword_3 import TypeKeyword3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class Keyword3(TypeKeyword3):
    """
    Detail information of keywords.

    Parameters
    ----------
    text
        Information for a keyword.
    """

    class Meta:
        name = "Keyword"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    text: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "max_occurs": 999,
        },
    )
