from __future__ import annotations

from dataclasses import dataclass

from .site_component_ref_structure import SiteComponentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntranceRefStructure(SiteComponentRefStructure):
    pass
