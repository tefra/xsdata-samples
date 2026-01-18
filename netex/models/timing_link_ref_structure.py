from __future__ import annotations

from dataclasses import dataclass

from .link_ref_structure import LinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingLinkRefStructure(LinkRefStructure):
    pass
