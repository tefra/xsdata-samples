from __future__ import annotations

from dataclasses import dataclass

from .entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ConventionalModeOfOperation2(DataManagedObjectStructure):
    class Meta:
        name = "ConventionalModeOfOperation_"
        namespace = "http://www.netex.org.uk/netex"
