from dataclasses import dataclass
from netex.models.alternative_texts_rel_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Organisation1(DataManagedObjectStructure):
    class Meta:
        name = "Organisation_"
        namespace = "http://www.netex.org.uk/netex"
