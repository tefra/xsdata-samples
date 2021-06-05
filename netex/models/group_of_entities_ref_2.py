from dataclasses import dataclass
from netex.models.version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfEntitiesRef2(VersionOfObjectRefStructure):
    class Meta:
        name = "GroupOfEntitiesRef_"
        namespace = "http://www.netex.org.uk/netex"
