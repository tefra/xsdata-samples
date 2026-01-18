from __future__ import annotations

from dataclasses import dataclass

from .retail_service_ref_structure import RetailServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailServiceRef(RetailServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
