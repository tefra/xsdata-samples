from __future__ import annotations

from dataclasses import dataclass

from .line_in_direction_ref_structure import LineInDirectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineInDirectionRef(LineInDirectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
