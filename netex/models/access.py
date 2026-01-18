from __future__ import annotations

from dataclasses import dataclass

from .access_version_structure import AccessVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Access(AccessVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
