from dataclasses import dataclass
from netex.models.alternative_texts_rel_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataManagedObjectViewStructure(DataManagedObjectStructure):
    class Meta:
        name = "DataManagedObject_ViewStructure"
