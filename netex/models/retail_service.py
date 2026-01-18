from __future__ import annotations

from dataclasses import dataclass

from .retail_service_version_structure import RetailServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailService(RetailServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
