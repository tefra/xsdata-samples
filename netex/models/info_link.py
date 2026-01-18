from __future__ import annotations

from dataclasses import dataclass

from .info_link_structure import InfoLinkStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InfoLink(InfoLinkStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
