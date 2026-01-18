from __future__ import annotations

from dataclasses import dataclass

from .subscribing_ref_structure import SubscribingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SubscribingRef(SubscribingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
