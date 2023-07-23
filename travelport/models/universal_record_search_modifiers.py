from __future__ import annotations
from dataclasses import dataclass
from travelport.models.base_search_modifiers import BaseSearchModifiers

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class UniversalRecordSearchModifiers(BaseSearchModifiers):
    """
    Controls and switches for the Universal Record Search request.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"
