from __future__ import annotations

from dataclasses import dataclass

from .connection_version_structure import ConnectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Connection(ConnectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
