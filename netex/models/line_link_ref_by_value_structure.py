from __future__ import annotations

from dataclasses import dataclass

from .link_ref_by_value_structure import LinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineLinkRefByValueStructure(LinkRefByValueStructure):
    pass
