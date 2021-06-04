from dataclasses import dataclass
from netex.models.data_managed_object_view_structure import DataManagedObjectViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataManagedObjectView(DataManagedObjectViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
