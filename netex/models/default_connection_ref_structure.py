from __future__ import annotations

from dataclasses import dataclass

from .connection_ref_structure import ConnectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DefaultConnectionRefStructure(ConnectionRefStructure):
    pass
