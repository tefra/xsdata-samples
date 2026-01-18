from __future__ import annotations

from dataclasses import dataclass

from .retail_consortium_version_structure import (
    RetailConsortiumVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailConsortium(RetailConsortiumVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
