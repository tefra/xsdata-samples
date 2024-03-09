from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_keyword_1 import TypeKeyword1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class Keyword1(TypeKeyword1):
    """
    Detail information of keywords.
    """

    class Meta:
        name = "Keyword"
        namespace = "http://www.travelport.com/schema/common_v52_0"
