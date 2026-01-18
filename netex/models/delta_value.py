from __future__ import annotations

from dataclasses import dataclass

from .delta_value_structure import DeltaValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeltaValue(DeltaValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
