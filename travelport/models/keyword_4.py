from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_keyword_4 import TypeKeyword4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class Keyword4(TypeKeyword4):
    """
    Detail information of keywords.
    """

    class Meta:
        name = "Keyword"
        namespace = "http://www.travelport.com/schema/common_v37_0"
