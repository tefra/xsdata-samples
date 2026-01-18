from __future__ import annotations

from dataclasses import dataclass

from .entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransportTypeAbstract(DataManagedObjectStructure):
    class Meta:
        name = "TransportType_"
        namespace = "http://www.netex.org.uk/netex"
