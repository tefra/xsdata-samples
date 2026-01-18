from __future__ import annotations

from dataclasses import dataclass

from .derived_view_structure import DerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DerivedView(DerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
