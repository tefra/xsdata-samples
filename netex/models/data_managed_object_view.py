from __future__ import annotations

from dataclasses import dataclass

from .data_managed_object_view_structure import DataManagedObjectViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataManagedObjectView(DataManagedObjectViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
