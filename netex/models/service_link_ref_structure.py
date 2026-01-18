from __future__ import annotations

from dataclasses import dataclass

from .timing_link_ref_structure import TimingLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceLinkRefStructure(TimingLinkRefStructure):
    pass
