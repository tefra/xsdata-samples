from dataclasses import dataclass

from .entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DayTypeAbstract(DataManagedObjectStructure):
    class Meta:
        name = "DayType_"
        namespace = "http://www.netex.org.uk/netex"
