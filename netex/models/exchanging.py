from __future__ import annotations

from dataclasses import dataclass

from .exchanging_version_structure import ExchangingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Exchanging(ExchangingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
