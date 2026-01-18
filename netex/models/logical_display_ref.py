from __future__ import annotations

from dataclasses import dataclass

from .logical_display_ref_structure import LogicalDisplayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LogicalDisplayRef(LogicalDisplayRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
