from __future__ import annotations

from dataclasses import dataclass, field

from .luggage_carriage_enumeration import LuggageCarriageEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageCarriageFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: LuggageCarriageEnumeration = field(
        default=LuggageCarriageEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
