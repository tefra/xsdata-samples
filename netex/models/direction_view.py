from __future__ import annotations

from dataclasses import dataclass

from .direction_derived_view_structure import DirectionDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DirectionView(DirectionDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
