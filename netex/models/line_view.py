from __future__ import annotations

from dataclasses import dataclass

from .line_derived_view_structure import LineDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineView(LineDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
