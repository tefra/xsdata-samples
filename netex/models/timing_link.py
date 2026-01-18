from __future__ import annotations

from dataclasses import dataclass

from .timing_link_version_structure import TimingLinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingLink(TimingLinkVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
