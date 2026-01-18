from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .luggage_carriage_enumeration import LuggageCarriageEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageCarriageFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[LuggageCarriageEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
