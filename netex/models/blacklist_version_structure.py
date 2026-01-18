from __future__ import annotations

from dataclasses import dataclass

from .security_list_version_structure import SecurityListVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BlacklistVersionStructure(SecurityListVersionStructure):
    class Meta:
        name = "Blacklist_VersionStructure"
