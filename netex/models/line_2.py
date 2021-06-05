from dataclasses import dataclass
from netex.models.alternative_texts_rel_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Line2(DataManagedObjectStructure):
    class Meta:
        name = "Line_"
        namespace = "http://www.netex.org.uk/netex"
