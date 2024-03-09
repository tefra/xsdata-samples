from dataclasses import dataclass, field
from typing import List

from .luggage_carriage_enumeration import LuggageCarriageEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LuggageCarriageFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[LuggageCarriageEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
