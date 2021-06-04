from dataclasses import dataclass
from netex.models.general_group_of_entities_ref_structure import GeneralGroupOfEntitiesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeneralGroupOfEntitiesRef(GeneralGroupOfEntitiesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
