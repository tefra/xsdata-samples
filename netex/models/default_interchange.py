from __future__ import annotations

from dataclasses import dataclass

from .default_interchange_version_structure import (
    DefaultInterchangeVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DefaultInterchange(DefaultInterchangeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
