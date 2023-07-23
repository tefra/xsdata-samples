from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_keyword_6 import TypeKeyword6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class Keyword6(TypeKeyword6):
    """
    Detail information of keywords.
    """
    class Meta:
        name = "Keyword"
        namespace = "http://www.travelport.com/schema/common_v38_0"
