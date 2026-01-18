from __future__ import annotations

from dataclasses import dataclass

from .entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UsageParameter2(DataManagedObjectStructure):
    class Meta:
        name = "UsageParameter_"
        namespace = "http://www.netex.org.uk/netex"
