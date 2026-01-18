from __future__ import annotations

from dataclasses import dataclass

from .security_list_ref_structure import SecurityListRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SecurityListRef(SecurityListRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
