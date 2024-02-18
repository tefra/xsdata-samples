from dataclasses import dataclass
from .alternative_texts_rel_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DayType2(DataManagedObjectStructure):
    class Meta:
        name = "DayType_"
        namespace = "http://www.netex.org.uk/netex"
