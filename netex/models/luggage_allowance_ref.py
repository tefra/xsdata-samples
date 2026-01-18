from __future__ import annotations

from dataclasses import dataclass

from .luggage_allowance_ref_structure import LuggageAllowanceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageAllowanceRef(LuggageAllowanceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
