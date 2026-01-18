from __future__ import annotations

from dataclasses import dataclass

from .blacklist_ref_structure import BlacklistRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BlacklistRef(BlacklistRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
