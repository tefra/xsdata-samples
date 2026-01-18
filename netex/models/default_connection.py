from __future__ import annotations

from dataclasses import dataclass

from .default_connection_version_structure import (
    DefaultConnectionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DefaultConnection(DefaultConnectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
