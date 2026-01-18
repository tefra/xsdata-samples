from __future__ import annotations

from dataclasses import dataclass

from .smartcard_ref_structure import SmartcardRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SmartcardRef(SmartcardRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
