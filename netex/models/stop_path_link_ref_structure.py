from __future__ import annotations

from dataclasses import dataclass

from .path_link_ref_structure import PathLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPathLinkRefStructure(PathLinkRefStructure):
    pass
