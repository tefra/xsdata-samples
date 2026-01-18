from __future__ import annotations

from dataclasses import dataclass

from .delta_value_structure import DeltaValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DeltaValue(DeltaValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
