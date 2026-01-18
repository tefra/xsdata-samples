from __future__ import annotations

from dataclasses import dataclass

from .default_connection_ref_structure import DefaultConnectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DefaultConnectionRef(DefaultConnectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
